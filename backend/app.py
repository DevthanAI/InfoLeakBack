from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Default page
    return "Hello world"


@app.route('/', methods=['GET, POST'])
def crawling():
    # Crawling page
    search_result = request.form['search_result']
    return jsonify({"search_result":search_result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
