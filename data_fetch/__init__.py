
import json
import logging

import azure.functions as func

from shared.config import AppConfig

logger = logging.getLogger(__name__)


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logger.info("HTTP trigger received a %s request.", req.method)

    config = AppConfig()

    if req.method == "GET":
        name = req.params.get("name", "World")

        response_body = {
            "method": "GET",
            "message": f"Hello, {name}!",
            "app_name": config.app_name,
            "query_params": dict(req.params),
        }
        return func.HttpResponse(
            body=json.dumps(response_body, indent=2),
            status_code=200,
            mimetype="application/json",
        )

    if req.method == "POST":
        try:
            body = req.get_json()
        except ValueError:
            return func.HttpResponse(
                body=json.dumps({"error": "Request body must be valid JSON."}),
                status_code=400,
                mimetype="application/json",
            )

        name = body.get("name", "World")

        response_body = {
            "method": "POST",
            "message": f"Hello, {name}!",
            "app_name": config.app_name,
            "received_body": body,
        }
        return func.HttpResponse(
            body=json.dumps(response_body, indent=2),
            status_code=200,
            mimetype="application/json",
        )