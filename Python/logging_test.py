import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is warning')
logger.error('This is an error')

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
  