class InvalidAgeException(Exception):
    def __init__(self, message, error_code = "BBC_ERR_CODE"):
        super().__init__(message)
        self.error_code = error_code


class Person:
    def __init__(self):
        self.age = 0

    def set_age(self, age):
        print("In set_age method")
        if isinstance(age,int) and age > 0 and age < 120:
            self._age = age
        else:
            raise InvalidAgeException("The age was wrong!", "ERR_API_XXX")


person = Person()

try:
    person.set_age(190)
except InvalidAgeException as exp:  # BBCApiError   # BBCXServiceError
    print("Looks like the age was wrong!")
    print(exp.error_code)

person._age = 10
