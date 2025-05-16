import logging

handlers = [logging.FileHandler('log.log'),
            logging.StreamHandler()]
logging.basicConfig(handlers=handlers,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)-8s - %(message)s')


x = 5

logging.debug(f"Logging debug for function {x}")
logging.info(f"Logging info for function {x}")
logging.warning(f"Logging warning for function {x}")
logging.error(f"Logging error for function {x}")
logging.critical(f"Logging critical for function {x}")
