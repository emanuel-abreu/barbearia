import json
from typing import Dict
from flask import Response


def generate_response(body:Dict[str,int | str],status:int=200, message:str=''):
    if message:
        body["message"] = message
    return Response(
        json.dumps(body, default=str), status=status, mimetype="application/json"
    )
