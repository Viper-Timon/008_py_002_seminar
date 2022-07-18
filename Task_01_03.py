# 3. Напишите программу, в которой
# пользователь будет задавать две строки,
# а программа - определять количество
# вхождений одной строки в другой.


print('введите искомую строку')
num1 = str(input())
print('введите вторую строку')
num2 = str(input())
count = 0

for i in range(len(num2)):
    k = 0
    for j in range(len(num1)):
        if i+j==len(num2):
            break
        elif num1[j] == num2[i+j]:
            k+=1
        else:
            break
    if k == len(num1):
        count += 1
if count == 0:
    print('Искомая строка не найдена')
else: print(count)
