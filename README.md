<h1 align="center"> YouTube Video Summarizer using LLaMA & Ollama </h1>
<p align="center">This Python tool automatically fetches the transcript of any YouTube video and generates a structured, concise summary using a local LLaMA model via Ollama
. It’s ideal for quickly summarizing long videos like tutorials, lectures, or podcasts into clear, actionable points.</p>

## 🚀 Features
- Automatic transcript extraction using youtube-transcript-api
- Concise AI-generated summaries using a LLaMA model (via Ollama)
- **Summaries include:**
  -  Main topic
  - Key points discussed
  - Short overall summary
  - Implementation steps (if applicable)
- Summary saved automatically to video_summary.txt
## 🧰 Tech Stack
-Python 3.8+
-youtube-transcript-api - for fetching YouTube subtitles
-Ollama – for running LLaMA locally
-LLaMA 2 model (or any other Ollama-supported model)
## 📦 Installation
-1️ Clone this repository
  git clone https://github.com/your-username/youtube-video-summarizer.git
  cd youtube-video-summarizer
- 2 Set up a Python virtual environment (recommended)
  python -m venv venv
  source venv/bin/activate   # On Mac/Linux
  venv\Scripts\activate      # On Windows
-3 Install dependencies
  pip install youtube-transcript-api ollama
- 4️ Install and set up Ollama
   -Download Ollama
     for your OS.
  - Pull the LLaMA 2 model (or another model you prefer):
  ollama pull llama2
Ensure the Ollama server is running in the background.

▶️ Usage

Run the script:

python summarize.py


Enter a YouTube video URL when prompted:

Enter youtube video url: https://youtu.be/fNk_zzaMoSs


The script will:

Extract the video ID from the URL

Fetch the transcript

Generate a structured summary using the LLaMA model

Print the summary in your terminal

Save the summary to video_summary.txt in the current directory

<h3 align="left">Connect with me:</h3>
<p align="left">
  <a href="mailto:deekshithapalvai@gmail.com" target="blank">
    <img align="center" src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="gmail" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/palvaireddy" target="blank">
    <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="palvaireddy" height="30" width="40" />
  </a>
</p>


---
