import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logs = [
        ("User login successful", "INFO"),
        ("Slow database response", "WARNING"),
        ("Database connection failed", "ERROR"),
        ("API timeout error", "ERROR")
    ]

    msg, level = random.choice(logs)

    if level == "INFO":
        logger.info(msg)
    elif level == "WARNING":
        logger.warning(msg)
    else:
        logger.error(msg)

    return {"message": msg}
