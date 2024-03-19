from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def Homepage():
    return render_template('main page.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')



if __name__ == '__main__':
    app.run(debug=True)