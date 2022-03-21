class RuntimeErrorWithCode(TypeError):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code

# doc string right under class definition - can be single line but still needs triple quotation marks

err = RuntimeErrorWithCode('An error happened.', 500)
print(err.__doc__)  # Gives you the doc string