from flask import Flask, render_template

app = Flask(__name__)

MENU = [
    {
        "name": "Classic Espresso",
        "category": "THE ORIGINAL",
        "description": "Bold, rich and beautifully simple. A little cup with a lot of character.",
        "price": 80,
        "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?auto=format&fit=crop&w=1000&q=85",
        "tag": "BOLD & BEAUTIFUL",
    },
    {
        "name": "Cappuccino",
        "category": "A CROWD FAVOURITE",
        "description": "A smooth espresso under a cloud of velvety milk foam.",
        "price": 120,
        "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?auto=format&fit=crop&w=1000&q=85",
        "tag": "CREAMY CLASSIC",
    },
    {
        "name": "Cold Coffee",
        "category": "COOL & REFRESHING",
        "description": "Chilled, creamy and made for slow afternoons and sunny days.",
        "price": 140,
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=1000&q=85",
        "tag": "CHILLED FAVOURITE",
    },
    {
        "name": "Café Mocha",
        "category": "A LITTLE INDULGENCE",
        "description": "Espresso and chocolate come together in one comforting cup.",
        "price": 150,
        "image":"/static/images/cafe-mocha.png",
        "tag": "COFFEE MEETS CHOCOLATE",
    },
    {
        "name": "Caramel Latte",
        "category": "SWEET MOMENTS",
        "description": "Silky espresso, steamed milk and a gentle caramel finish.",
        "price": 160,
        "image": "/static/images/Latte.png",
        "tag": "A TOUCH OF SWEETNESS",
    },
]

@app.route("/")
def home():
    return render_template("index.html", menu=MENU)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)