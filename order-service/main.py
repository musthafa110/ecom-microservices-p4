from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def get_orders():
    return [{"id": 1, "product": "Laptop"}, {"id": 2, "product": "Phone"}]
