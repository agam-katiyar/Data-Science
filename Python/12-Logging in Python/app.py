import logging

## basic logging settngs

logging.basicConfig(
    level = logging.DEBUG,
    format ='%(asctime)s - %(name)s - %(message)s',
    datefmt='%y-%m-%d  %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b} =  {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError: ## when b is zero
        logger.error("Division by zero error")
        return None


add(10,23)
subtract(15,5)
multiply(10,3)
divide(10,5)
divide(35,0)