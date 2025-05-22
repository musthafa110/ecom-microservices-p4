from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/products")
def get_products():
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]