import logging

#Each log has a severity level, which determines if it should be recorded (depending on level setting).

# Level	   Numeric Value	             Usage
# DEBUG	       10	                     Detailed info (dev use only)
# INFO	       20	                     General events (program flow)
# WARNING	   30	                     Something unexpected, but program continues
# ERROR	       40	                     Serious problem (operation failed)
# CRITICAL     50	                     Program may not recover

# 👉 Default logging level is WARNING, so debug and info won’t show unless you change it.


print("Before Changing Level:\n ----------------------- \n")
logging.debug("Debug message")  # Will not print if default(DEBUG) is not changed
logging.info("Info message") # Will not print if default(DEBUG) is not changed
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message\n")


# Confugure logging
logging.basicConfig(
    level=logging.DEBUG, #mininum log level to capture
    #force=True
)

print("After Changing Level:\n")

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message \n")


# It will still not print Info and Debug because of the following reasons
# We called logging.warning(...) before any explicit configuration.
# The logging module sees no handlers and auto-calls basicConfig() internally 
# with defaults (level=WARNING, a StreamHandler to stderr).
# Later calls to logging.basicConfig(...) are ignored because the root logger already has handlers.
# Result: root logger remains at WARNING and nothing is written to app.log.
#we can set force=True to forcefully change the handler and then print second statemsn

print("Handler's Name:",logging.getHandlerNames())
print(logging.getLogger(__name__))


