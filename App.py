from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, Flask!'

# Define a route for a dynamic URL
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

# Define a route that accepts GET and POST methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        return redirect(url_for('home'))
    return render_template('login.html')

# Start the development server
if __name__ == '__main__':
    app.run(debug=True)
