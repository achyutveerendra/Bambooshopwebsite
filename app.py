from flask import Flask, render_template

app = Flask(__name__)
PRODUCTS = [{
    'id': 1,
    'name': "Bamboos",
    'price': "200"
}, {
    'id': 2,
    'name': "Gampaa",
    'price': "200"
}, {
    'id': 3,
    'name': "Bamboo Stick",
    'price': "80"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', products=PRODUCTS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
