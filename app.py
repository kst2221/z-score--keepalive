from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ I'm alive!", 200

# Render는 기본적으로 0.0.0.0:10000 이상의 포트를 허용함
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
