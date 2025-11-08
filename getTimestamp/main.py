from flask import Flask, jsonify
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

# Adjust timezone if needed (e.g. +05:30 for IST)
IST = timezone(timedelta(hours=5, minutes=30))


@app.route("/")
def get_timestamp():
    current_time = datetime.now(IST).isoformat()
    return jsonify({"timestamp": current_time})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
