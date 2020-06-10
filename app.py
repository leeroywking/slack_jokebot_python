__version__ = '0.1.0'

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def joke():
    res = requests.get('https://icanhazdadjoke.com/',{},headers={'Accept':'text/plain'})
    print(res.content)
    return res.content

if __name__ == '__main__':
    app.run()