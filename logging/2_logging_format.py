
import logging

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


#If we do not configure our own logger, "roor" will appear in the log as this is the default

# Confugure logging
logging.basicConfig(
    level=logging.DEBUG, #mininum log level to capture
    format = "Line:%(lineno)s Time: %(asctime)s Name:%(name)s Level:%(levelname)s Process ID: %(process)d",
    filename="app.log", # Optional, saves log to file
    filemode = "w", # a = append, w = overwrite
    force=True
)

logging.debug("This is a Debug message")
