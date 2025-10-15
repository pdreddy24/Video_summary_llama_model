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

### 1️ Clone this repository
```bash
git clone https://github.com/your-username/youtube-video-summarizer.git
cd youtube-video-summarizer
### 2 Set up a Python virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
### 3 Install dependencies

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
