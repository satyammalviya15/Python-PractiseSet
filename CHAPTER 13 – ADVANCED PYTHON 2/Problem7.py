# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, Flask!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
