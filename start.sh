#!/bin/bash
apt update && apt install -y ffmpeg
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
