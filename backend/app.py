from flask import Flask, jsonify, request
from crawling_function import crawl_driver
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def index():
    # Default page
    return "Hello world"


@app.route('/crawling', methods=['POST'])
def crawling():
    # Crawling page
    data = request.get_json()
    init_info_front = data['init_info']
    return crawl_driver(keywords=init_info_front)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
