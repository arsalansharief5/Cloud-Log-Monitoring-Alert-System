# Cloud Log Monitoring & Alert System

## Project Overview
This project implements a cloud-native log monitoring and alerting system using AWS managed services.  
It automatically detects error logs from a Lambda application and sends real-time email alerts using an event-driven architecture.

The system demonstrates cloud monitoring, observability, and alert automation following DevOps best practices.

---

## Technologies Used

![AWS](https://custom-icon-badges.demolab.com/badge/AWS-%23FF9900.svg?logo=aws&logoColor=white)
![AWS Lambda](https://custom-icon-badges.demolab.com/badge/AWS%20Lambda-%23FF9900.svg?logo=aws-lambda&logoColor=white)
![CloudWatch](https://custom-icon-badges.demolab.com/badge/CloudWatch-FF4F8B?logo=amazoncloudwatch&logoColor=white)
![SNS](https://custom-icon-badges.demolab.com/badge/Amazon%20SNS-FF9900?logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)
![VS Code](https://custom-icon-badges.demolab.com/badge/VS%20Code-0078d7.svg?logo=visualstudiocode&logoColor=white)

- AWS Lambda – Application and log analyzer functions  
- Amazon CloudWatch Logs – Log collection and filtering  
- CloudWatch Dashboards – Metrics visualization  
- Amazon SNS – Alert notifications via email  
- Python – Lambda function implementation  

---

## Architecture Overview
The system follows an event-driven architecture:

1. A sample Lambda application generates logs (success & error).
2. CloudWatch Logs captures all application logs.
3. A subscription filter streams error logs to a log analyzer Lambda.
4. The analyzer processes logs and publishes alerts to an SNS topic.
5. SNS sends email notifications to subscribed users.
6. CloudWatch Dashboard visualizes invocations and errors.

Architecture diagram and detailed explanation are available in the `architecture/` folder.

---

## Key Features
- Real-time error detection from Lambda logs
- Automated email alerts using SNS
- Centralized log monitoring
- Custom CloudWatch dashboard
- Serverless and cost-efficient design
- AWS Free Tier compatible

---

## Project Structure

```
cloud-log-monitoring-alert-system/
│
├── architecture/
├── cloudwatch/
├── lambda/
├── screenshots/
├── sns/
└── README.md
```

## Monitoring Dashboard
The CloudWatch dashboard provides visibility into:
- Lambda invocations for the sample application
- Lambda error count
- Log analyzer Lambda invocations
- Recent application error logs

The dashboard configuration is stored in: `cloudwatch/dashboard.json`

---

## Alerting Mechanism
- Error logs are detected using a CloudWatch Logs subscription filter
- Alerts are published to an SNS topic
- Email notifications are sent to confirmed subscriber

SNS setup and configuration details are documented in: `sns/sns-setup.md`

---

## Lessons Learned
- SNS email subscriptions must be confirmed before alerts are delivered
- CloudWatch Logs subscription filters enable real-time log analysis
- Serverless architectures simplify monitoring and alerting pipelines
- Dashboards provide quick visibility into system health

---

## Cost Considerations
This project is designed to run entirely within the AWS Free Tier:
- No EC2 instances used
- No paid search or analytics services
- Low Lambda invocation volume

---

## Use Case
This system can be used for:
- Application error monitoring
- DevOps observability demonstrations
- Foundation for production alerting pipelines

---

## Author

**Arsalan Sharief**  
Cloud & DevOps Enthusiast  

<div align="center">
  <a href="https://linkedin.com/in/arsalansharief5">
    <img src="https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/arsalansharief5">
    <img src="https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="mailto:arsalansharief5@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
</div>