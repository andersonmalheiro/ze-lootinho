from flask import Flask, json

from controllers.get_gpus import get_gpus

app = Flask(__name__)


@app.route("/gpus/nvidia")
def get():
    data = get_gpus()

    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json',
        content_type='application/json',
        status=200,
    )
    return response
