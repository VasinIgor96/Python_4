s=13
e=33
begin = end =-1
begin = int(input('Enter a begin: '))
end = int(input('Enter an end: '))

if begin > end:
    begin, end = end, begin
else:
    begin, end = end, begin
while begin < s or begin > e:
      begin = int(input("Enter"))
while end < s or end > e:
      end = int(input("Enter"))
for i in range(begin, end +1):
    if i %2 !=0:
       print(i)