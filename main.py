from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """
