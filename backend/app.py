from flask import Flask, jsonify, request
from crawling_function import crawl_driver

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Default page
    return "Hello world"


@app.route('/crawling', methods=['POST'])
def crawling():
    # Crawling page
    data = request.get_json()
    init_info_front = data['init_info']
    # Example
    # initial_information = ["soolee0701", "soojlee0106",
    #                        "ofdetectivesandcats", "010-8839-2919"]

    return crawl_driver(keywords=init_info_front)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
