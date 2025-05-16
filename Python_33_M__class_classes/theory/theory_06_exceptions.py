class CustomException(Exception):
    pass


try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(e)  # This is a custom exception
