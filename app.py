from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "PW Render API Running ✅"

@app.route("/pw")
def pw():
    url = request.args.get("url")
    token = request.args.get("token")

    if not url:
        return "URL missing", 400

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.youtube.com/"
    }

    try:
        r = requests.get(url, headers=headers, stream=True)
        return Response(
            r.iter_content(chunk_size=1024),
            content_type=r.headers.get("Content-Type")
        )
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
