from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.get(
    '/html-response', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def get_html():
    return """
    <html>
        <body>
            <p class="enfase">Olá mundo em HTML</p>
        </body>
        <style>
        .enfase{
            color:red;
            font-weight:bolder;
            text-decoration-line: underline;
        }
        </style>
    </html>
"""
