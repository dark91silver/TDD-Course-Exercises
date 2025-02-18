class WrongFormatDate(Exception):
    def __init__(self, text):
        super().__init__(text)

class WrongIntervalDate(Exception):
    def __init__(self, text):
        super().__init__(text)

class WrongFormatInput(Exception):
    def __init__(self, text):
        super().__init__(text)
