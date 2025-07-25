from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(
    model="llama3"
)

template = """
You are an expert in answering questions about a pizza restaurant but you feel sad today.

Here are some relvant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    question = input("Ask your question (q to quit): ")
    if question == 'q':
        break
    reviews= retriever.invoke(question) # grab the relevant revies
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)