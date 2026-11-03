from flask import Flask
import requests

app = Flask(__name__)

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'


@app.route('/response')
def get_response():
    resp = requests.get(url)

    info = resp.json()
    print(info[0])

    return "Hello Jeff"










if __name__ == "__main__":
    app.run(debug= True)
