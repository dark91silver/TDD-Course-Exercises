class MissingIdException(Exception):
    def __init__(self, text):
        super().__init__(text)

class MissingFieldException(Exception):
    def __init__(self, text):
        super().__init__(text)

class WrongDateFormatException(Exception):
    def __init__(self, text):
        super().__init__(text)

class WrongPaymentFormatException(Exception):
    def __init__(self, text):
        super().__init__(text)

class NegativePaymentException(Exception):
    def __init__(self, text):
        super().__init__(text)

class MissingInputException(Exception):
    def __init__(self, text):
        super().__init__(text)