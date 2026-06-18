# Import logging module

import logging


# Configure logger

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("Automation Started")

logging.info("Reading CSV File")

logging.info("Login Process Completed")

print("Log file created")
