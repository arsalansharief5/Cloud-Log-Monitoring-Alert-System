# SNS Alert Setup

This document explains how I configured Amazon SNS to send email alerts when errors are detected in the system.

---

## Purpose of SNS in This Project

Amazon SNS is used to:
- Send real-time email notifications when application errors occur
- Receive alerts from the log analyzer Lambda function
- Notify stakeholders immediately without manual monitoring

---

## SNS Topic Creation

1. Open **AWS SNS Console**
2. Click **Topics**
3. Click **Create topic**
4. Choose:
   - Type: **Standard**
   - Name: `cloud-log-alerts`
5. Click **Create topic**

---

## SNS Topic ARN

> arn:aws:sns:us-east-1:xxxxxxxxxxxx:cloud-log-alerts **(replace ARN)**

> **Note:** Account number partially blurred for public sharing.

This ARN is used inside the log analyzer Lambda function to publish alert messages.

---

## Email Subscription Setup

1. Open the SNS topic: `cloud-log-alerts`
2. Click **Create subscription**
3. Configure:
   - Protocol: `Email`
   - Endpoint: `your-email@gmail.com` **(replace email)**
4. Click **Create subscription**

After creating the subscription, an email confirmation request was sent.

---

## Subscription Confirmation

- Opened the confirmation email from AWS SNS
- Clicked **Confirm subscription**
- Verified that the subscription status changed to **Confirmed** in the SNS console

Without confirmation, SNS messages are not delivered.

---

## Common Pitfall & Lesson Learned

Initially, alert emails were not received even though the SNS topic and Lambda integration were correctly configured.

- **Root cause:**  
The email subscription was still in a **PendingConfirmation** state.

- **Resolution:**  
After opening the SNS confirmation email and clicking **Confirm subscription**, alerts started arriving immediately.

- **Lesson:**  
SNS email subscriptions must be explicitly confirmed before messages are delivered. Always verify the subscription status is **Confirmed** in the SNS console.

---

## Integration with Lambda

- The SNS Topic ARN is configured as an environment variable in the `log-analyzer` Lambda
- When an error pattern is detected in logs, the Lambda publishes a message to this SNS topic
- SNS then sends the alert to the confirmed email subscriber

---

## Alert Behavior

- Each detected error triggers a new SNS notification
- Email includes:
  - Error message
  - Timestamp
  - Log source information
- Alerts are delivered within seconds of the error occurring

---

## Security & Cost Notes

- Only one email subscription is used
- SNS is triggered only when error events occur
- All resources are within AWS Free Tier limits during development

---

## Summary

SNS enables immediate awareness of application failures by pushing alerts via email, completing the event-driven monitoring flow of the system.
