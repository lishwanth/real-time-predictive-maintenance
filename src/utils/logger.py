import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    return logger

# Example Usage
if __name__ == "__main__":
    logger = get_logger("TestLogger")
    logger.info("This is an info message")
