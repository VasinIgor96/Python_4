

begin = int(input("Введіть початкове число діапазону: "))
end = int(input("Введіть кінцеве число діапазону: "))

if begin > end:
    begin, end = end, begin
print("\n")
# Виведення усіх чисел діапазону
print("Виведення усіх чисел діапазону: ")
for i in range(begin, end+1):
        print(i, end="\n")
        print()
# Виведення чисел діапазону за спаданням
print("Виведення чисел діапазону за спаданням: ")
for i in range(end, begin -1,-1):
        print (i, end="\n")
        print()
# Виведення усіх чисел кратних 7
print("Виведення усіх чисел кратних 7: ")
for i in range(begin, end+1):
    if i %7 == 0:
        print(i, end="\n")
        print()
# Кількість чисел кратних 5
count = 0
for i in range(begin, end+1):
    if i %5 == 0:
        count += 1
print("Кількість чисел кратних 5: ",count)