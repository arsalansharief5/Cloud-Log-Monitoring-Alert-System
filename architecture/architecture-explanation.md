# Architecture Explanation  
Cloud Log Monitoring & Alert System

## Overview
This project implements a **serverless cloud log monitoring and alert system** using AWS managed services.  
The system automatically detects application errors from logs and sends **real-time email alerts** without managing any servers.

The architecture follows an **event-driven, serverless design**, ensuring scalability, low cost, and minimal operational overhead.

---

## Architecture Components

### 1. Sample Application Lambda (`sample-log-app`)
- A Python-based AWS Lambda function.
- Simulates application behavior by generating logs of different levels:
  - INFO
  - WARNING
  - ERROR
- Logs are written automatically to **Amazon CloudWatch Logs**.
- Used to demonstrate how real application logs are monitored.

---

### 2. Amazon CloudWatch Logs
- Centralized log storage and monitoring service.
- Collects logs emitted by the `sample-log-app` Lambda function.
- Acts as the **log ingestion layer** of the system.
- Stores logs securely and enables filtering and subscription mechanisms.

---

### 3. CloudWatch Logs Subscription Filter
- A subscription filter is configured on the log group of `sample-log-app`.
- Filter pattern used: ERROR
- Ensures that **only error-level logs** are forwarded for further processing.
- This reduces unnecessary processing and improves efficiency.

---

### 4. Log Analyzer Lambda (`log-analyzer`)
- Triggered automatically by the CloudWatch subscription filter.
- Receives compressed and encoded log data from CloudWatch.
- Decodes and analyzes each log entry.
- Checks for the presence of `ERROR` messages.
- When an error is detected, it publishes an alert message to Amazon SNS.

---

### 5. Amazon SNS (Simple Notification Service)
- Used as the alerting mechanism.
- A topic named `cloud-log-alerts` is created.
- The `log-analyzer` Lambda publishes messages to this topic.
- An email subscription is attached to the topic.
- Delivers **real-time email notifications** to the user whenever an error occurs.

---

## End-to-End Flow

1. `sample-log-app` Lambda executes and generates logs.
2. Logs are automatically sent to **CloudWatch Logs**.
3. Subscription filter detects `ERROR` logs.
4. Filtered logs trigger the `log-analyzer` Lambda.
5. `log-analyzer` processes the logs and identifies errors.
6. An alert message is sent to the SNS topic.
7. SNS delivers an email notification to the subscribed user.

---

## Architectural Benefits

- **Serverless**: No servers to manage or maintain.
- **Cost-efficient**: Runs entirely within AWS Free Tier for testing and demos.
- **Scalable**: Automatically scales with log volume.
- **Event-driven**: reacts instantly to error events.
- **Production-relevant**: Mimics real-world cloud monitoring systems used in industry.

---

## Use Cases

- Application error monitoring
- Production log analysis
- Alerting and incident notification
- DevOps and SRE workflows

---

## Conclusion
This architecture demonstrates a real-world **cloud-native monitoring pipeline** using AWS Lambda, CloudWatch, and SNS.  
It is suitable for small applications, learning environments, and production-ready alerting systems.

