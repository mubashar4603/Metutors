from utilities.customLogger import LogGen
# Create a logger instance using the loggen method
logger = LogGen.loggen()

# Log an example message
logger.info("This is an example log message")

# Log a warning message
logger.warning("This is a warning message")
