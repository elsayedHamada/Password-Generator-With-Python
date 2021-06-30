import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
numbers = "1234567890"
symbols = "!@#$%^&*()_+=-?><|}{\\][:`~'"

upper_choose = input("Do You Want To Use Upper Case Letters In The Password y/n >>").lower()
lower_choose = input("Do You Want To Use lower Case Letters In The Password y/n >>").lower()
numbers_choose = input("Do You Want To Use numbers Case Letters In The Password y/n >>").lower()
symbols_choose = input("Do You Want To Use symbols Letters In The Password y/n >>").lower()

add = ""

if upper_choose == "y":
    add += upper_case
if lower_choose == "y":
    add += lower_case
if numbers_choose == "y":
    add += numbers
if symbols_choose == "y":
    add += symbols
else:
    print("Ok")
    
length = int(input("What The Length of your password >> "))
password_num = int(input("How Many Password Do you want generate >> "))

print("\n")
print("Generated Password >> ")
print("-----------------------")

for x in range(password_num):
    password = "".join(random.sample(add, length))
    print(password)