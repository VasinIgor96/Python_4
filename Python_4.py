
begin = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for i in range(begin, end+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Це число кратне 3 та 5","'Fizz Buzz'")
    elif i % 3 == 0:
        print("Це число кратне 3","'Fizz'")
    elif i % 5 == 0:
        print("Це число кратне 5","'Buzz'")
    else:
        print("Це число не кратне ні 3, ні 5: ",i)