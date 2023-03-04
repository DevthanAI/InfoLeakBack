from flask import Flask, request, jsonify
from crawling_api import get_results

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Default page
    return "Hello world"


@app.route('/', methods=['GET, POST'])
def crawling():
    # Crawling page
    intial_information = request.form['intial_information']
    search_results = get_results(intial_information)
    return jsonify({"search_results": search_results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
