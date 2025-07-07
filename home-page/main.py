from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>eCommerce Home</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #f0f4f8, #d9e2ec);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            .container {
                background-color: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }

            h1 {
                color: #2c3e50;
                margin-bottom: 10px;
            }

            p {
                color: #555;
                margin-bottom: 30px;
            }

            a.button {
                display: inline-block;
                padding: 12px 24px;
                margin: 10px;
                font-size: 16px;
                color: white;
                background-color: #3498db;
                border: none;
                border-radius: 6px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }

            a.button:hover {
                background-color: #2980b9;
            }

            footer {
                margin-top: 30px;
                font-size: 14px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛍️ Welcome to FastShop</h1>
            <p>Your one-stop solution for tech gadgets and online orders.</p>
            <a class="button" href="/product">Browse Products</a>
            <a class="button" href="/order">View Your Orders</a>
            <footer>Powered by FastAPI • DevOps CI/CD Demo</footer>
        </div>
    </body>
    </html>
    """

