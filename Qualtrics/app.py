from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # This will load your main HTML page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)
