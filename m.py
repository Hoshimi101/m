# 1

number = int(input("Введите двузначное число: "))

tens = number // 10 
digits = number % 10

summa_digils = tens + digits
mulliply_digitls = tens * digits

print(f"В числе {number} находится {tens} десятков и {digits}")
print(f"Сумма цифр {tens} + {digits} = {summa_digits}\nПроизведение цифр {tens} * {digits} = {multiply_digitls}")

# 2

number = int(input("Введите двузначное число: "))
tens = number // 10
digits = number % 10

itog1 = int(str(digits) + str(tens))
itog2 = digits * 10 + tens * 1 

print(itog1, itog2)

# 3
number = int(input("Введите трёзначное число: "))
tens = (number // 10) 
digits = number % 10
hundred = number // 100

print(tens, digits, hundred)

# 4

# Дано:

pl = 99
gh = 25
hb = 12

# Решение:

rew = pl (gh * 12)
print(f"Стоимость поезки: {rew} руб.")

# 5
 
number = int(input("Введите число: "))

class1 = str({number})
class2 = int({number})

# 10 

count_peoples = int(input("Введите кол-во пассажиров: "))
count_mest = int(input("Введите кол-во места в одной машине: "))
payments_car = float(input("Введите стоимость одной машины: "))
people_payment = float(input("Какую сумму каждый готов заплатить: "))


summa_payments_peoples = count_peoples * people_payment #10 * 100 -> 1000


cars = (count_peoples + count_mest - 1) // count_mest #10 + 3 -> 13 // 4 -> 3
total_cars = cars * payments_car #3 * 200 -> 600 


per_person = total_cars / count_peoples #600 / 10 -> 60.0


print("Машин", cars)
print(f"Всего: {total_cars:.2f} руб.")
print(f"С каждого: {per_person:.2f} руб.")
print(f"Бюджет хватает: {per_person <= people_payment}")
print(count_peoples, cars, sep="/")
