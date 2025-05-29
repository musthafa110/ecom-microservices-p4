from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Order Service</title>
        </head>
        <body>
            <h1>Welcome to the Order Service</h1>
            <h3>Order #1001</h3>
            <p>Status: Shipped</p>
            <p>History: Ordered on 2025-05-20, Processed on 2025-05-21, Shipped on 2025-05-23</p>

            <h3>Order #1002</h3>
            <p>Status: Processing</p>
            <p>History: Ordered on 2025-05-22, Processing started on 2025-05-23</p>

            <h3>Order #1003</h3>
            <p>Status: Delivered</p>
            <p>History: Ordered on 2025-05-18, Processed on 2025-05-19, Shipped on 2025-05-20, Delivered on 2025-05-22</p>
        </body>
    </html>
    """
