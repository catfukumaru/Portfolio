from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
# from https://www.youtube.com/watch?v=E4l91XKQSgw

# vector search is a databse that is stored in the computer using chroma db
# it is used to look at info quickly that can be given to the model

#df=data frame
df = pd.read_csv("realistic_restaurant_reviews.csv") #load the csv file
embeddings = OllamaEmbeddings(model="mxbai-embed-large") 
# Ollama Embeddings class is used to generate vector embeddings from text using embedding models. These embeddings are long arrays of numbers that represent the semantic meaning of the input text. The class allows for the configuration of various parameters to control the embedding generation process, such as the model to use, truncation settings, and other options related to computation and sampling.
# The Ollama Embeddings class can be integrated with tools like LangChain and LlamaIndex to support retrieval augmented generation (RAG) applications, where embeddings are used to search for similar data in a database


db_location = "./chrome_langchain_db" # where to store the database
add_documents = not os.path.exists(db_location) # checks if the database exits in the location

if add_documents: # if ther is no database
    documents = []
    ids = [] # this is to check that the ids are not diffrent from the ones in documents

    for i, row in df.iterrows(): # iterate through the rows
        document = Document(
            page_content= row["Title"] + " " + row["Review"], # what you are going to be looking up
            metadata = {"rating": row["Rating"], "date": row["Date"]}, # additional data that will not be used in the query
            id = str(i) # an id
        )# makes a document - storing a piece of text and associated metadata.


        ids.append(str(i))
        documents.append(document)
    

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location, # where to store is permanetly so that it does not need to be remade every time the ai runs
    embedding_function=embeddings # the embeddings model
) 

# Vector stores are specialized data stores that enable indexing and retrieving information based on vector representations.
#A vector database, vector store or vector search engine is a database that uses the vector space model to store vectors (fixed-length lists of numbers) along with other data items.

# These vectors, called embeddings, capture the semantic meaning of data that has been embedded.

# Vector stores are frequently used to search over unstructured data, such as text, images, and audio, to retrieve relevant information based on semantic similarity rather than exact keyword matches. 

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids) # add documents to the vector store if the databse does not exits

retriever = vector_store.as_retriever( # to make the data useable by the llm. 
    search_kwargs= {"k": 5} # number of documents it should look up
)