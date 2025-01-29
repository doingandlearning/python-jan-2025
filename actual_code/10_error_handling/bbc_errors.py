"""
BBC_ERR_CODE =
BBC_API_WITH_STORYBOOK =
"""
class InvalidAgeException(Exception):
    def __init__(self, message, error_code = "BBC_ERR_CODE"):
        super().__init__(message)
        self.error_code = error_code


