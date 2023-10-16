from validators import ValidationFailure
import validators


class URLInput:
    def __init__(self, url):
        self.url = url
        self.valid = False

    def check(self):
        result = validators.url(self.url)
        if isinstance(result, ValidationFailure):
            self.valid = False
        else:
            self.valid = True
        return self.valid

    def get_valid(self):
        return self.valid
