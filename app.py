from flask import Flask
from utils import visitor_counter


app = Flask(__name__)


@app.route("/")
def home():
    new_count = visitor_counter()

    f = open("visitor_count.txt", "w")
    f.write(new_count)
    f.close()

    return f"Visitor Count: {new_count}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
