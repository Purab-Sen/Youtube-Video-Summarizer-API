from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import dotenv_values

video_retriever_map = {}
api_key = dotenv_values()["GOOGLE_API_KEY"]


def getRetriever(video_id):
    if video_id in video_retriever_map:
        return video_retriever_map[video_id]
    #fetch the video transcripts
    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id,languages=["en"])
        transcripts = " ".join(chunk.text for chunk in transcript_list)
    except TranscriptsDisabled:
        print("No captions available for this video id")
    
    #split the transcripts into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.create_documents([transcripts])
    #find their embeddings and store in vector store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",api_key=api_key)
    vector_store = FAISS.from_documents(chunks,embeddings)

    #creating retriever
    retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})
    video_retriever_map[video_id] = retriever
    return retriever