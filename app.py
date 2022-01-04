from flask import Flask, render_template
import config

app = Flask(__name__)


environment = "production"
if environment == "development":
   cfg = config.DevelopmentConfig()
elif environment == "production":
   cfg = config.ProductionConfig()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
