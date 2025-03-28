from fastapi import FastAPI, HTTPException
import os
import subprocess
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "YouTube Shorts Generator API is Live!"}

@app.post("/generate/")
def generate_short(video_url: str, start_time: str = "00:00:30", duration: str = "00:00:15"):
    try:
        output_filename = "short_clip.mp4"

        # Step 1: Download YouTube Video using yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Step 2: Cut the Short Clip using FFmpeg
        ffmpeg_command = f"ffmpeg -i video.mp4 -ss {start_time} -t {duration} -vf scale=1080:1920 -y {output_filename}"
        subprocess.run(ffmpeg_command, shell=True, check=True)

        return {"status": "success", "message": "Short clip generated!", "download_url": "/download/short_clip.mp4"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
