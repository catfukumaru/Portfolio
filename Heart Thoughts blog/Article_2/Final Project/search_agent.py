# from https://www.youtube.com/watch?v=9KKnNh89AGU
import ollama
import sys_msgs
import requests
import trafilatura #s rapes text from a from any site no matter the structre of the page
from bs4 import BeautifulSoup # crapes text from a specific site where we know the exca html structre of the page

from vector import retriever


assistant_convo = [sys_msgs.assistant_msg] # where the prompts and the responses from the assitant are stored. this variable will also be used by the assitant for context

# #######################################################################################
# functions for searhing ONLINE
# #######################################################################################

def search_or_not(): #an agent
    # decides if the prompt needs to be searched or not
    sys_msg = sys_msgs.search_or_not_msg # explains how the agent should work for this task

    response = ollama.chat(
        model='llama3:latest',
        messages=[{'role':'system', 'content': sys_msg}, assistant_convo[-1]]
    ) # makes an agent that gives a response

    content = response['message']['content'] # select the mesage content from the response. should return true or false only
    print(f'search online or not results: {content}') # to know what the agent has retturned

    if 'true' in content.lower():
        return True
    return False


def query_generator(): # an agent
    # makes a web search query to find the data the assitant needs to respond the query
    sys_msg = sys_msgs.query_msg
    query_msg = f'create a search query for this prompt: \n{assistant_convo[-1]}' # adds the last message in assistant_convo

    response = ollama.chat(
        model='llama3:latest',
        messages=[{'role':'system', 'content': sys_msg}, {'role': 'user','content': query_msg }]
    ) # generates the response

    return response['message']['content'] 


def  duckduckgo_search(query):
    # does the search and gets the data from the serch result. where you click to get to the web page
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36,"
    } # header settings for the web request. it mimics a web browser user

    url = f'https://duckduckgo.com/html/?q={query}' # the url with the query at the end
    response = requests.get(url, headers=headers) # where the search happens
    response.raise_for_status() # handles errors

    soup = BeautifulSoup(response.text, 'html.parser') # get the text from the html parser. it makes an organized structure of the html scrapped
    results = [] # keeps the structured data from the search resutls
    for i, result in enumerate(soup.find_all('div', class_='result'), start=1): # loop through each of the search result elements. enumerate is used to keep track of the resutls
        if i > 10: # gets the first 10 results
            break

        title_tag = result.find('a', class_='result__a') # get the clickable title of the search result
        if not title_tag:
            continue
    
        link = title_tag['href'] # the link to the sear result
        snippet_tag= result.find('a', class_='result__snippet') # the search description for the result
        snippet = snippet_tag.text.strip() if snippet_tag else 'No description available'

        results.append({
            'id':i, 
            'link': link,
            'search_descripition': snippet

        })

    return results # now how up to 10 strucuures search results 


def best_search_results(s_results, query):
    # chooses the best search result from the 10
    sys_msg = sys_msgs.best_search_msg
    best_msg = f'SEARCH QUERY: {s_results} \nUSER_PROMPT: {assistant_convo[-1]} \nSEARCH QUERY: {query}'

    for _ in range(2): # it is hard for ai to do this so they are given a second chance
        try:
            response = ollama.chat(
                model='llama3:latest',
                messages=[{'role':'system', 'content': sys_msg}, {'role': 'user', 'content': best_msg}]

            )
        
            return int(response['message']['content']) # should return a number from 0 - 9 which is the index for the search result
        
        except: # goes to the second attempt on the loop or ends the loop or it is not a number
            continue

    return 0 # if an integer was not returned. chooses the first search result as the best one

def scrape_webpage(url):
    try:
        downloaded = trafilatura.fetch_url(url=url)
        return trafilatura.extract(downloaded, include_formatting=True, include_links=True) # returns the data without the html code but with a ny spacing and otther formatting
    except Exception as e:
        return None

def ai_search():
    # defines the order and the logic of how the  agent should be used. returns the correct web search contech that can be used with prompts
    context = None 
    print('generating search query') # to know which agent is working
    search_query = query_generator()

    
    # removes quotes
    if search_query[0] == '"':
        search_query = search_query[1:-1] # removes the quotes

    search_results = duckduckgo_search(search_query)
    context_found = False

    while not context_found and len(search_results) > 0: # looks through the 10 search reuslts 
        best_result = best_search_results(s_results=search_results, query=search_query)
        try:
            page_link = search_results[best_result]['link'] # the link from the best result
        except:
            print('could not choose the best search result, trying again')
            continue

        page_text = scrape_webpage(page_link) # the data from the actual page
        search_results.pop(best_result) # remove the result from search_results

        if page_text and contains_data_needed(search_content=page_text, query=search_query): #if page_text exists  and the data from the page is relevant
            context = page_text
            context_found = True

    return context
        

def contains_data_needed(search_content, query):
    # removes duplicate or irrelevant data to reduce hallucinations and does not fill the respose with useless stuff when it does not find data

    sys_msg = sys_msgs.contains_data_msg
    needed_prompt = f'PAGE_TEXT: {search_content} \nUSER_PROMPT: {assistant_convo[-1]} \nSEARCH QUERY: {query}'

    response = ollama.chat(
                model='llama3:latest',
                messages=[{'role':'system', 'content': sys_msg}, {'role': 'user', 'content': needed_prompt}]

            )
    content = response['message']['content']
    
    if 'true' in content.lower():
        return True
    else:
        return False

def stream_assitant_response():
    global assistant_convo # so that changes to it can be saved
    response_stream = ollama.chat(model = 'llama3:latest', messages=assistant_convo, stream=True) # used to generate the response. assistant_convo is passed from context
    #  the process of delivering data from a server to a client in chunks as it becomes available, rather than waiting for the entire response to be generated before sending it
    complete_respose = '' # the token made from ollama will be in tihs variable so that it can be added to assitant_convo once the stream is complete
    print('ASISTANT: ')

    for chunk in response_stream: # loop through each chucnk from the stream as it is generated
        print(chunk['message']['content'], end='', flush=True) # print the message content from the chunk 
        # Flushing the stream refers to the process of forcing the contents of an output stream to be immediately transferred from the buffer to the destination
        # This is particularly useful when you want to ensure that data is written out right away, rather than waiting for the buffer to fill up or the stream to close.
        complete_respose += chunk['message']['content']

    assistant_convo.append({'role': 'assistant', 'content' : complete_respose})
    print("\n\n")



# #######################################################################################
# functions for searhing PDFs
# #######################################################################################

def search_documents_or_not():
    # decides if the prompt needs to be searched or not
    sys_msg = sys_msgs.search_PDF_or_not_msg # explains how the agent should work for this task

    response = ollama.chat(
        model='llama3:latest',
        messages=[{'role':'system', 'content': sys_msg}, assistant_convo[-1]]
    ) # makes an agent that gives a response

    content = response['message']['content'] # select the mesage content from the response. should return true or false only
    print(f'search documents or not results: {content}') # to know what the agent has retturned

    if 'true' in content.lower():
        return True
    return False


def main():
    global assistant_convo

    while True: # conversation functionality
        prompt = input('USER: \n')
        
        assistant_convo.append({'role': 'user', 'content' : prompt}) # add the user input in a specific format to assistant_convo

        if search_documents_or_not(): # search documents should be first but that is just a matter of chaning the under of the if-ifelse block
            # check if the data needed is in the retirever
            print("This really needs a search")
            reviews= retriever.invoke(prompt) # grab the relevant revies / this would be context that would help the ai answer the question
            assistant_convo = assistant_convo[:-1]

            if reviews: # if context was found. since it will return none if it finds no context
                    prompt = f'SEARCH RESULT: {reviews} \n\nUSER PROMPT: {prompt}'
            else:    # failed attempt at web search       
                prompt = (
                    f'USER PROMPT: \n{prompt} \n\nFAILED SEARCH: \nThe '
                    'AI search model was unable to extract any reliable data. Explain that '
                    'and ask if the user would like you to search again or respond '
                    'without web search context. Do not respond if a search was needed ' 
                    'and you are getting this message with anything but the above request '
                    'of how the user would like to proceed'
                )

            assistant_convo.append({'role': 'user', 'content': prompt}) # add the allama formatted prompt to the assistant_convo

            
            
        else:
            if search_or_not():
                context = ai_search()
                assistant_convo = assistant_convo[:-1] # if the web search was done then remove the last prompt 

                if context: # if context was found. since it will return none if it finds no context
                    prompt = f'SEARCH RESULT: {context} \n\nUSER PROMPT: {prompt}'
                else:    # failed attempt at web search       
                    prompt = (
                        f'USER PROMPT: \n{prompt} \n\nFAILED SEARCH: \nThe '
                        'AI search model was unable to extract any reliable data. Explain that '
                        'and ask if the user would like you to search again or respond '
                        'without web search context. Do not respond if a search was needed ' 
                        'and you are getting this message with anything but the above request '
                        'of how the user would like to proceed'
                    )

                assistant_convo.append({'role': 'user', 'content': prompt}) # add the allama formatted prompt to the assistant_convo

        stream_assitant_response()


if __name__ == '__main__':
    main()
