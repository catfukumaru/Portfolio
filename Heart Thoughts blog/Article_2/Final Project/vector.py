from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os


from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document



# vector search is a databse that is stored in the computer using chroma db
# it is used to look at info quickly that can be given to the model

#df=data frame
#df = pd.read_csv("realistic_restaurant_reviews.csv") #load the csv file

FOLDER_PATH= r"C:\\Users\ranun\\Documents\\Local-LLM-projects\\ollama-project1\\ai_merge_projects\\pdf_documents"

# todo: make a function to see if all the files in a directory are pdfs
def load_documents():
    document_loader = PyPDFDirectoryLoader(FOLDER_PATH) # loads all the documents in the folder
    return document_loader.load()

pdf_documents = load_documents()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50, )

all_splits = text_splitter.split_documents(pdf_documents)

#print(all_splits[0])
# what are the parts of this. watch the guys video

db_location = "./chrome_langchain_db" # where to store the database
add_documents = not os.path.exists(db_location) # checks if the database exits in the location

if add_documents: # if ther is no database
    documents = []
    ids = [] # this is to check that the ids are not diffrent from the ones in documents

    for i, chunk in enumerate(all_splits): # iterate through the rows
        document = Document(
            page_content= chunk.page_content, # what you are going to be looking up
            metadata = {'subject': chunk.metadata.get('subject'), 'title': chunk.metadata.get('title'), 'page': chunk.metadata.get('page'), 'pag_label': chunk.metadata.get('page_label'), 'author': chunk.metadata.get('author')}, 
            id = str(i)
            )

        ids.append(str(i))
        documents.append(document)
    
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location, # where to store is permanetly so that it does not need to be remade every time the ai runs
    embedding_function=embeddings # the embeddings model
) 


if add_documents:
    vector_store.add_documents(documents=documents, ids=ids) # add documents to the vector store if the databse does not exits

retriever = vector_store.as_retriever( # to make the data useable by the llm. 
    search_kwargs= {"k": 5} # number of documents it should look up
)

