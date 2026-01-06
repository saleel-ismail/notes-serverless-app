import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("table-note")

def lambda_handler(event, context):
    method = event.get("requestContext", {}) \
                  .get("http", {}) \
                  .get("method")

    # ---------- GET ----------
    if method == "GET":
        response = table.scan()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(response.get("Items", []))
        }

    # ---------- POST ----------
    if method == "POST":
        body = event.get("body", "{}")
        data = json.loads(body)

        item = {
            "note-id": str(uuid.uuid4()),
            "title": data.get("title"),
            "content": data.get("content")
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(item)
        }

    # ---------- FALLBACK ----------
    return {
        "statusCode": 405,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "error": "Method not allowed"
        })
    }
