
begin = int(input("������ ������� ��������: "))
end = int(input("������ ����� ��������: "))

if begin > end:
    begin, end = end, begin

for i in range(begin, end+1):
    if i % 2 != 0:
        print(i)






