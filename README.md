# YouTube Video Helper (RAG-based)

**AI-powered Streamlit app for interactive Q&A on YouTube videos using Retrieval-Augmented Generation (RAG), LangChain, and OpenAI.**

---

## 🚀 Features

- **Transcript Retrieval:** Automatically fetches YouTube video transcripts.
- **Semantic Search:** Chunks and embeds transcripts for fast, relevant retrieval.
- **RAG Pipeline:** Combines retrieval and generation for accurate, context-aware answers.
- **Multi-language Support:** Select transcript language (e.g., English, Hindi).
- **Modern UI:** Clean, interactive Streamlit interface.

---

## 🖥️ Demo

![App Screenshot](https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png)

---

## 🛠️ Tech Stack

- **Streamlit** – UI framework
- **LangChain** – Text splitting, retrieval, and chaining
- **OpenAI** – Embeddings & LLM (GPT-4o-mini)
- **Chroma** – Vector store for semantic search
- **youtube-transcript-api** – Transcript extraction

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/youtube-video-helper.git
cd youtube-video-helper
pip install -r requirements.txt
```

---

## ⚡ Usage

1. **Run the app:**
    ```bash
    streamlit run Main.py
    ```
2. **Enter a YouTube video ID.**
3. **Select transcript language from the sidebar.**
4. **Ask any question about the video.**
5. **Get instant, context-aware answers!**

---

## 📝 Example

- Enter: `cQDsYfftXTg`
- Ask: `Summarize the main points of this video.`

---

## 📚 How It Works

1. **Transcript Extraction:**  
   Retrieves transcript using `youtube-transcript-api`.

2. **Chunking & Embedding:**  
   Splits transcript and embeds chunks with OpenAI.

3. **Retrieval-Augmented Generation:**  
   Uses LangChain to retrieve relevant chunks and generate answers via GPT-4o-mini.

---

## 💡 Project Highlights

- Retrieval-Augmented Generation (RAG) architecture
- End-to-end semantic search and answer generation
- User-friendly, responsive UI

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

## 📄 License

MIT

---

**Made with ❤️ using Streamlit, LangChain, and OpenAI**

---

> _For resume: Developed a RAG-based Streamlit app for interactive Q&A on YouTube videos. Automated transcript retrieval, semantic search, and context-aware answer generation using LangChain and OpenAI._
