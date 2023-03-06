from flask import Flask, jsonify, request
from crawling_function import crawl_driver

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def index():
    # Default page
    return "Hello world"


@app.route('/crawling', methods=['GET', 'POST'])
def crawling():
    # Crawling page
    initial_information = request.form['intial_information']
    # Example
    # initial_information = ["soolee0701", "soojlee0106",
    #                        "ofdetectivesandcats", "010-8839-2919"]
    info_list = crawl_driver(keywords=initial_information)
    return jsonify({"info_list": info_list})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
