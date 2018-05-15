
import json
import asyncio
import aiohttp

from flask import Flask, current_app, render_template
from flask_aiohttp import AioHTTP
from flask_aiohttp.helper import async, websocket

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4qwQ8z\n\xec]/'

aio = AioHTTP(app)

@app.route('/', defaults={'arg': 'Index'}) 
@app.route('/<arg>')
@async
def index(arg):
    data = {
        'data': arg
    }

    data = json.dumps(data)
    current_app.response_class(data, headers={
        'Content-Type': 'application/json',
    }, status=201)
    return render_template('index.html', arg=data)


def main():
    aio.run(app, debug=True)

if __name__ == '__main__':
    main()