def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            return error.args[0] if error.args else "Error accessing contacts"
        except ValueError as error:
            return error.args[0] if error.args else "Wrong format of input data"
        except IndexError as error:
            return "Not enough count of arguments"
        except FileNotFoundError as error:
            return error.args[0] if error.args else "Help file not found"
    return inner