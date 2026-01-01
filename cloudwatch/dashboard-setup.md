# CloudWatch Dashboard Setup

This document explains how I created the CloudWatch dashboard for monitoring the Lambda-based log monitoring system using the AWS Console.

---

## Purpose of the Dashboard

The dashboard provides a single view to:
- Monitor Lambda invocations and errors
- Observe how often the log analyzer Lambda runs
- View recent application logs in near real-time

This helps in quickly identifying failures and understanding system behavior.

---

## Dashboard Creation Steps

### 1. Create Dashboard

1. Open **AWS CloudWatch**
2. Navigate to **Dashboards**
3. Click **Create dashboard**
4. Enter name: `cloud-log-monitoring-dashboard`
5. Click **Create dashboard**

---

## 2. Add Lambda Invocations Widget (sample-log-app)

1. Click **Add widget**
2. Select **Line** chart
3. Click **Next**
4. On the widget configuration screen, switch to the **Editor** tab  
   (instead of using the Metric Builder)
5. Used **Metric Insights query editor** to define the metric manually

### Configuration used:
- Namespace: `AWS/Lambda`
- Metric: `Invocations`
- Dimension: `FunctionName`
- Value: `sample-log-app`
- Statistic: `Sum`
- Period: `5 minutes`

This widget shows how many times the application Lambda is invoked.

---

## 3. Add Lambda Errors Widget (sample-log-app)

1. Click **Add widget**
2. Select **Line** chart
3. Click **Next**
4. Switched to the **Editor** tab
5. Used Metric Insights to query error counts

### Configuration used:
- Namespace: `AWS/Lambda`
- Metric: `Errors`
- Dimension: `FunctionName`
- Value: `sample-log-app`
- Statistic: `Sum`
- Period: `5 minutes`

This widget helps identify when errors occur in the application Lambda.

---

## 4. Add Lambda Invocations Widget (log-analyzer)

1. Click **Add widget**
2. Select **Line**
3. Click **Next**
4. Used the **Editor tab** again instead of Metric Builder
5. Filtered metrics for `log-analyzer` Lambda

### Configuration used:
- Namespace: `AWS/Lambda`
- Metric: `Invocations`
- Dimension: `FunctionName`
- Value: `log-analyzer`
- Statistic: `Sum`
- Period: `5 minutes`

This shows how often the log analyzer is triggered by log events.

---

## 5. Add Log Insights Widget

1. Click **Add widget**
2. Select **Logs**
3. Click **Next**
4. Selected the log group: `/aws/lambda/sample-log-app`
5. Used **CloudWatch Logs Insights** query editor

### Query used:
```
SOURCE "/aws/lambda/sample-log-app"
| fields @timestamp, @message
| sort @timestamp desc
| limit 10000
```

This widget displays the latest application logs directly on the dashboard.

---

## Final Result

- Metrics widgets are placed on the top row for quick visibility
- Log widget is placed below to inspect errors immediately
- The dashboard updates automatically as Lambda functions run
- The dashboard configuration is stored as JSON in dashboard.json for version control and reuse.