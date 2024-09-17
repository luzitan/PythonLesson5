"""
Задача 1: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""

def stepen(a, b):
    if b == 1:
        return a
    return a * stepen(a, b - 1)


a = int(input("Число а: "))
b = int(input("Число b: "))
print(stepen(a,b))