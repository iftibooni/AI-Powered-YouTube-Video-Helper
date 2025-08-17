from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st


load_dotenv()


st.title("YouTube Video Helper")
st.write("This app helps learning from YouTube videos using their transcripts.")

# Add a sidebar for branding and instructions
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png", width=80)
st.sidebar.title("YouTube Helper")
st.sidebar.markdown("""
**Instructions:**
1. Enter a valid YouTube video ID .
2. Ask any question about the video.
3. Get answers from the transcript!
""")

# Add a header and some spacing
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #ffffff;'>🎬 Transcript Q&A</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Style the input boxes
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: #f9f9f9;
        border-radius: 8px;
        border: 1px solid #000000;
        padding: 8px;
        color: #000000; /* <-- This makes the input text black */
    }
    .stButton>button {
        background-color: #FF0000;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

video_id = st.text_input("Enter a Youtube Video ID Here:")

if video_id:
    api = YouTubeTranscriptApi()
    transcripts = api.fetch(video_id, languages=['en'])    
else:
    st.error("Please enter a valid YouTube video ID.")

#text is separated from timestamps

transcript_list = [snippet.text for snippet in transcripts.snippets]
transcript=transcript_list
full_transcript = ' '.join(transcript_list)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([full_transcript])

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
)

vector_store.add_documents(chunks)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})


parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

user_question = st.text_input("Ask a question about the video:")
if user_question:
    result = main_chain.invoke(user_question)
    st.write(result)
else:
    st.write("Please ask a question to get started.")