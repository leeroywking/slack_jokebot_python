__version__ = '0.1.0'

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def joke():
    res = requests.get('https://icanhazdadjoke.com/',{},headers={'Accept':'text/plain'})
    print(res.content)
    dataobj = {"text":res.content}
    requests.post('https://hooks.slack.com/services/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', data=dataobj)
    
    return res.content

if __name__ == '__main__':
    app.run()


