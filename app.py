from flask import Flask, jsonify
import requests

app = Flask(__name__)

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'


@app.route('/response')
def get_response():
    resp = requests.get(url)

    info = resp.json()
    

    return jsonify(info)










if __name__ == "__main__":
    app.run( port=5555, debug= True)
