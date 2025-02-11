from flask import Flask, render_template, request
from key import *  # Import your API Key from key.py file
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword')  # Get the keyword entered by the user
    if keyword:
        url = f"https://newsapi.org/v2/everything?q={keyword}&language&fr&apiKey={apiKey}"
    else:
        url = f"https://newsapi.org/v2/everything?q=cybersécurité&language&fr&apiKey={apiKey}"

    req = requests.get(url)
    res = req.json()
    articles = res.get("articles")
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=False)