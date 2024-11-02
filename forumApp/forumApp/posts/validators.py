from typing import List
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadLanguageValidator:
    def __init__(self, words: List, message=None):
        self.words = words
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.message = 'Please DO Not use bad language'
        else:
            self.__message = value

    def __call__(self, value):
        for word in self.words:
            if word.lower() in value.lower():
                raise ValidationError(self.message)


# class DigitValidator:
#     def __int__(self, message=None):
#         self.message = message
#
#     @property
#     def message(self):
#         return self.__message
#
#     @message.setter
#     def message(self, value):
#         if not value:
#             self.message = 'Please DO Not use digits'
#         else:
#             self.__message = value
#
#     def __call__(self, value):
#         for char in value:
#             if char.isdigit():
#                 raise ValidationError('The title must not have integers')
