# 📽️ YouTube Video Summarizer with LLaMA & Transcripts

This project automatically fetches the transcript of any YouTube video and generates a **short, structured summary** using an LLM (LLaMA model via [Ollama](https://ollama.ai)). It’s ideal for quickly extracting **key insights, takeaways, and implementation steps** from long videos like tutorials, lectures, or podcasts.

---

## 🚀 Features

- ✅ **Automatic transcript extraction** using [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)  
- 📝 **Concise AI-generated summaries** using a LLaMA model (via Ollama)  
- 🧠 **Summaries include**:
  - Main topic  
  - Key points discussed  
  - Short overall summary  
  - Implementation steps (if applicable)  
- 💾 Summary saved automatically to `video_summary.txt`

---

## 🧰 Tech Stack

- **Python 3.8+**  
- [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) – for fetching YouTube subtitles  
- [Ollama](https://ollama.ai/) – for running LLaMA locally  
- **LLaMA 2 model** (or any other Ollama-supported model)

---

## 📦 Installation

### **1️⃣ Clone this repository**
- Run the following commands in your terminal:
  - git clone https://github.com/your-username/youtube-video-summarizer.git
  -cd youtube-video-summarizer

## **2️⃣ Set up a Python virtual environment**
- Create and activate a virtual environment:
  - python -m venv venv
  - source venv/bin/activate (Mac/Linux)
  - venv\Scripts\activate (Windows)

## **3️⃣ Install dependencies** 

- Install the required packages:

  -pip install -r requirements.txt

## **4️⃣ Install and set up Ollama**
- Download Ollama
   - for your OS. Pull the LLaMA 2 model (or another model you prefer):
  - ollama pull llama2
- Ensure the Ollama server is running in the background.
## ▶️ Usage 

- Run the script:

  - python summarize.py
- Enter a YouTube video URL when prompted, for example:
  - https://youtu.be/fNk_zzaMoSs

 The script will:

  - Extract the video ID from the URL
  
  - Fetch the transcript
  
  - Generate a structured summary using the LLaMA model
  
  - Print the summary in your terminal
  
  - Save the summary to video_summary.txt in the current directory
