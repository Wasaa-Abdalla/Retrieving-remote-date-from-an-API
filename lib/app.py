from flask import Flask, render_template
from lib.get_requester import GetRequester

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    employees = requester.load_json()
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
