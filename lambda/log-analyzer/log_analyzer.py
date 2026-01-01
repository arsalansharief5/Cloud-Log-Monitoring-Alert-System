import json
import boto3
import gzip
import base64

sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:XXXXXXXXXXXX:cloud-log-alerts"

def lambda_handler(event, context):
    # Decode CloudWatch log data
    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    log_data = json.loads(uncompressed_payload)

    error_messages = []

    # Check each log event
    for log_event in log_data['logEvents']:
        message = log_event['message']
        if "ERROR" in message or "Exception" in message:
            error_messages.append(message)

    # Send email alert if errors found
    if error_messages:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Cloud Log Monitoring Alert",
            Message="\n".join(error_messages)
        )

    return {
        "statusCode": 200,
        "body": "Log processing completed"
    }
