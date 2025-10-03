import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function to generate a pre-signed S3 URL.
    Supports both upload (PUT) and download (GET).
    """

    # Read bucket name from environment variable
    bucket_name = os.environ.get("BUCKET_NAME")

    # Parse input event
    try:
        body = json.loads(event["body"])
        file_name = body["file_name"]
        operation = body.get("operation", "get_object")  # default is GET
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Invalid input: {str(e)}"})
        }

    # Validate operation
    if operation not in ["get_object", "put_object"]:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Operation must be 'get_object' or 'put_object'"})
        }

    try:
        # Generate pre-signed URL (valid for 1 hour)
        url = s3_client.generate_presigned_url(
            ClientMethod=operation,
            Params={"Bucket": bucket_name, "Key": file_name},
            ExpiresIn=3600
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "file_name": file_name,
                "operation": operation,
                "presigned_url": url
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
