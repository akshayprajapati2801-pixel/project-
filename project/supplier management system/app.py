from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Supplier Management System is Running!"

if __name__ == "__main__":
    app.run(debug=True)