import json
import boto3
import uuid
from datetime import datetime, timezone

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

table = dynamodb.Table("GenAIChatHistory")

MODEL_ID = "amazon.nova-micro-v1:0"


def lambda_handler(event, context):

    try:

        # -----------------------------
        # 1. Get request body
        # -----------------------------

        body = event.get("body")

        if isinstance(body, str):
            body = json.loads(body)

        question = body.get("question", "").strip()

        if not question:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "error": "Question is required"
                })
            }

        # -----------------------------
        # 2. Call Amazon Bedrock
        # -----------------------------

        response = bedrock.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": question
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 300,
                "temperature": 0.7
            }
        )

        # -----------------------------
        # 3. Extract AI response
        # -----------------------------

        answer = response["output"]["message"]["content"][0]["text"]

        # -----------------------------
        # 4. Save conversation
        # -----------------------------

        session_id = str(uuid.uuid4())

        table.put_item(
            Item={
                "sessionId": session_id,
                "question": question,
                "answer": answer,
                "timestamp": datetime.now(
                    timezone.utc
                ).isoformat()
            }
        )

        # -----------------------------
        # 5. Return result
        # -----------------------------

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": True,
                "question": question,
                "answer": answer
            })
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
