#importing packages
from youtube_transcript_api import YouTubeTranscriptApi
import os
import ollama

#get youtube urls
#youtube_url="https://youtu.be/fNk_zzaMoSs?si=6kswvHZaDU19GbHM&t=1"
#youtube_url ="https://www.youtube.com/watch?v=fNk_zzaMoSs&t=1"
#youtube_url = "https://youtu.be/ry9SYnV3svc?si=BkcbpDtNa9hir-PL&t=1"
youtube_url = input("Enter youtube video url: ")


#get video ID
def extract_video_id(youtube_url):
    if "youtube.com" in youtube_url:
        return youtube_url.split("?v=")[-1].split("&")[0]
    elif "youtu.be" in youtube_url:
        return youtube_url.split(".be/")[-1].split("?")[0]
    
video_id = extract_video_id(youtube_url)
#print(video_id)    

#fetching api
youtube_api = YouTubeTranscriptApi()
youtube_transcript = youtube_api.fetch(video_id)

#print(youtube_transcript)
lis_transcript =[text.text for text in youtube_transcript]
full_transcript = " ".join(lis_transcript)


#ai prompt
prompt = """ create a short and concise summary of the video  based on the following transcript.
    the goal is to create a summary that captures the main points and key takeaways from the video.
    provide the answer in a markdown format with appropriate headings and subheadings.
    highlight the following sections clearly:
    1. the main topic of the video
    2. key points discussed in the video
    3. short overall summary
    4. clear steps to implement the ideas taught is the video(If applicable)
    
    here is the transcript:
    """ +full_transcript
    
#print("prompt:", prompt)

response = ollama.generate(model="llama2",prompt = prompt)
print("--------summary-------")
print(response["response"])



filename = "video_summary.txt"
with open(filename, 'w') as f:
    f.write[response["response"]]

