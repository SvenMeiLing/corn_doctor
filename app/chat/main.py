from flask import Flask
from flask import request, render_template, jsonify, Response
from flask_cors import CORS
from spark_chat import chat

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.get("/")
def index():
    return render_template(r"index.html")


@app.post("/coderv")
def coderv():
    code = request.json.get("code")
    print(request.method)

    def ext_gen(code):
        for g in chat(code):
            yield g.content

    print(list(ext_gen(code)))
    return Response(ext_gen(code), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
