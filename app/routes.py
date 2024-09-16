import logging
import os

from app import create_app
from app.utils import generate_response

logging.basicConfig(level=logging.INFO)
app = create_app(os.getenv("FLASK_CONFIG"))


@app.route("/", methods=["GET"])
def get_subscribers():
    return generate_response({"message": "Hello, world!"})
