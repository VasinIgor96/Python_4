

begin = int(input('Enter a begin: '))
end = int(input('Enter an end: '))

for i in range(begin, end+1):
    if i %2 !=0:
        print(i)
