from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head><title>Product Service</title></head>
        <body>
            <h1>Products</h1>
            <h3>1. Smartphone X100 - $799</h3>
            <p>6.5" OLED, Octa-core 2.8GHz, 8GB RAM, 128GB Storage, 48MP Camera</p>

            <h3>2. Laptop Pro 15 - $1499</h3>
            <p>15.6" FHD, Intel i7, 16GB RAM, 512GB SSD, NVIDIA GTX 1650</p>

            <h3>3. Wireless Headphones Z3 - $199</h3>
            <p>30h Battery, Bluetooth 5.0, Active Noise Cancellation, 250g</p>
        </body>
    </html>
    """
