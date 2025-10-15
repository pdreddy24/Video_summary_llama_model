# 📽️ YouTube Video Summarizer with LLaMA & Transcripts

This project automatically fetches the transcript of any YouTube video and generates a **short, structured summary** using an LLM (LLaMA model via [Ollama](https://ollama.ai)). It’s ideal for quickly extracting **key insights, takeaways, and implementation steps** from long videos like tutorials, lectures, or podcasts.

---
## 🧠 My Insights
While building this project, I got a deeper understanding of how local LLM inference works using Ollama. Instead of relying on cloud APIs, Ollama allows models like LLaMA 2 to run completely on a local machine. It acts like a mini server that listens for prompts and returns generated responses, which gave me a practical sense of how language models are deployed in real-world pipelines.
## 📖 What I Understood About the Model
- Ollama provides a local runtime for models like LLaMA 2, meaning the model weights are stored and executed on my machine.
- My Python script communicates with this local server through the ollama Python library, sending the transcript and prompt for summarization.
- The prompt quality is crucial — a well-structured prompt leads to clean, structured summaries (main topic, key points, implementation steps).
- I learned how the model doesn’t understand the video itself — it relies entirely on the transcript text and the clarity of the instructions given.
## How I Used It

- I extracted the video transcript using youtube-transcript-api.

- I created a detailed summarization prompt containing clear instructions.

- I passed this prompt to LLaMA 2 through Ollama’s local interface to generate a concise summary.

- Finally, I displayed and saved the output automatically to a .txt file.

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
## **Output**
# Main Topic
Explains the basics of linear algebra using intuitive visualizations.

## Key Points
- Importance of vectors and matrices
- Geometric interpretation of linear transformations
- How linear algebra applies to real-world problems

## Summary
The video simplifies linear algebra concepts through clear visuals and real-world examples.

## Implementation Steps
1. Practice vector operations using online tools
2. Solve transformation problems manually
3. Explore applications in data science and ML

## **Notes & Limitations**

- Videos must have subtitles enabled for transcripts to work.

- Some videos may have auto-generated transcripts with limited accuracy.

- The quality of the summary depends on the model and transcript quality.

- Make sure Ollama is running before executing the script.

## **📌 Future Improvements**

-  Add support for summarizing videos in different languages

 - Handle transcripts that exceed model context length (chunking)
 - Add a simple Streamlit or Gradio web UI


<h3 align="left">Connect with me:</h3>
<p align="left">
  <a href="mailto:deekshithapalvai@gmail.com" target="blank">
    <img align="center" src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="gmail" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/palvaireddy" target="blank">
    <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="palvaireddy" height="30" width="40" />
  </a>
</p>

