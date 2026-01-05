from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import dotenv_values
from retrievers import getRetriever
from utility import format_docs


api_key = dotenv_values()["GOOGLE_API_KEY"]


#Augmentation
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.2,api_key=api_key)
prompt = PromptTemplate(
    template="""
       You are a helpful assistant.
       Answer ONLY from the provided transcript context.
       If the context is insufficient, just say "I don't have enough information".

       {context}
       Question: {question}
    """,
    input_variables=['context','question']
)
parser = StrOutputParser()



def get_answer_of_question(video_id,question):
    retriever = getRetriever(video_id)
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question':RunnablePassthrough()
    })


    main_chain = parallel_chain | prompt | llm | parser #parallel chain
    answer = main_chain.invoke(question)
    return answer
