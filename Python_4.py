
begin = int(input("¬вед≥ть початок д≥апазону: "))
end = int(input("¬вед≥ть к≥нець д≥апазону: "))

if begin > end:
    begin, end = end, begin

for i in range(begin, end+1):
    if i % 2 != 0:
        print(i)






