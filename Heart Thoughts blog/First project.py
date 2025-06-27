from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate # converst the user input and parameters into instructions for the llm
# it selects part of the user response to then use to give better answers
template = """
Answer the question below.
Here is the conversation history: {context}

Question: {question}

Answer:
"""
# context and question are variables in the template

model = OllamaLLM(model="llama3") # gets the model
prompt = ChatPromptTemplate.from_template(template) # make a template from the template string
chain = prompt | model # a chain, the results of the promt is passed on to the model

def handle_conversation():
    context = "" # the chat does not end with one question-response
    print("Welcome user, Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input == 'exit': # a way to quit the program
            break


        result = chain.invoke({"context": context, "question": user_input}) # passing the variables in the format of the template in to the model
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}" # the current question-response is kept


if __name__ == "__main__":
    handle_conversation()