from flask import Flask, render_template, url_for, request

import os

app = Flask(__name__)

# Path to the videos directory
VIDEO_FOLDER = "static/videos"
THUMBNAIL_FOLDER = "static/thumbnails"

@app.route("/")
def catalog():
    """
    Display a catalog of available videos.
    """
    videos = [
        {
            "name": video.split(".")[0],
            "thumbnail": url_for("static", filename=f"thumbnails/{video.split('.')[0]}.jpg"),
            "path": url_for("static", filename=f"videos/{video}")
        }
        for video in os.listdir(VIDEO_FOLDER)
        if video.endswith(".mp4")
    ]
    return render_template("catalog.html", videos=videos)

@app.route("/play/<video_name>")
def play(video_name):
    """
    Play the selected video.
    """
    video_path = url_for("static", filename=f"videos/{video_name}.mp4")
    return render_template("player.html", video_path=video_path, video_name=video_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug="True")
