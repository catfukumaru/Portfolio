from gnewsclient import gnewsclient
 
# declare a NewsClient object 
client = gnewsclient.NewsClient(language='english', location='UK', max_results=10)
 
# get news feed
client.get_news()
##Write a Python program that retrieves the top stories from Google News.
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-8.php