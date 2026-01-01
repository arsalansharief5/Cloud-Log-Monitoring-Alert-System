# CloudWatch Subscription Filter Configuration

## Purpose
The subscription filter connects Amazon CloudWatch Logs to the `log-analyzer` Lambda function.  
It ensures that only **error-level logs** are forwarded for processing.

---

## Log Group
- Log Group Name: /aws/lambda/sample-log-app
- This log group is automatically created when the `sample-log-app` Lambda runs.

---

## Subscription Filter Details

- Destination: AWS Lambda
- Target Lambda Function: `log-analyzer`
- Filter Pattern: ERROR
- Filter Name: error-log-filter

---

## How It Works

1. `sample-log-app` generates application logs.
2. Logs are stored in CloudWatch Logs.
3. Subscription filter scans incoming logs.
4. Only logs containing the keyword `ERROR` are selected.
5. Matching logs are streamed in near real-time to the `log-analyzer` Lambda.

---

## Benefits

- Reduces unnecessary processing
- Improves system efficiency
- Enables real-time error detection
- Mimics production-grade log monitoring systems

---

## Notes
- The filter pattern is case-sensitive.
- Multiple subscription filters can be added for different log levels if required.
