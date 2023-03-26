
begin = int(input('Enter a begin: '))
end = int(input('Enter an end: '))
if begin > end:
   begin, end = end, begin
   
for i in range(end, begin -1,-1):
        print(i)