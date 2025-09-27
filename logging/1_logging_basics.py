import logging

#Each log has a severity level, which determines if it should be recorded (depending on level setting).

# Level	   Numeric Value	             Usage
# DEBUG	       10	                     Detailed info (dev use only)
# INFO	       20	                     General events (program flow)
# WARNING	   30	                     Something unexpected, but program continues
# ERROR	       40	                     Serious problem (operation failed)
# CRITICAL     50	                     Program may not recover

# 👉 Default logging level is WARNING, so debug and info won’t show unless you change it.


print("Before Changing Level:\n")
logging.debug("Debug message")  # Will not print if default(DEBUG) is not changed
logging.info("Info message") # Will not print if default(DEBUG) is not changed
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message\n")


# Confugure logging
logging.basicConfig(
    level=logging.INFO, #mininum log level to capture
    format = "%(asctime)s - %(name)s - %(levelname)s - %(lineno)s",
    filename="app.log", # Optional, saves log to file
    filemode = "a", # a = append, w = overwrite

)

logging.basicConfig(level=logging.INFO)
print("After Changing Level:\n")
logging.debug("Debug message")  # Will not print if default(DEBUG) is not changed
logging.info("Info message") # Will not print if default(DEBUG) is not changed
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")



# You can customize log output with format specifiers:

# Specifier	          Meaning
# %(asctime)s	      Timestamp
# %(levelname)s	      Logging level (INFO, ERROR, etc.)
# %(message)s	      Actual log message
# %(name)s	          Logger name
# %(filename)s	      File name of script
# %(lineno)d	      Line number of log call
# %(process)d	      Process ID
# %(thread)d	      Thread ID

