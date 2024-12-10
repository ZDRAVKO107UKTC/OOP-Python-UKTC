# class Calculator:
#     @staticmethod
#     def square(n):
#         return n * n
#
# print(Calculator.square(8))
#
# class String_Utils:
#     @staticmethod
#     def reverse_string(s):
#         return s[::-1]
#
# print(String_Utils.reverse_string(input()))

class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
age = int(input())
perso = Person.is_adult(age)
print(perso)