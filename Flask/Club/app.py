from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='app', static_url_path="/app")

@app.route("/resume")
def heartbeat():
    path =  "resume.html"
    return send_from_directory("app", path)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if not path or path == 'app':
        path = 'index.html'
    return send_from_directory("app", path)

if __name__ == "__main__":
    app.run(debug=True)
