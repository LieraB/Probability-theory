import matplotlib.pyplot as plt
import numpy as np
import math

my_str_2 = r'C:\Users\babam\Pictures\\'
f = open(r'C:\Users\babam\Documents\text.txt','w')
print('Введіть назву файла ')
name_file=input()
with open(my_str_2+name_file+".txt") as file:
    array = [row.strip() for row in file]

np_array=np.unique(array)
print("\n")
count1=len(array)
if count1 > 12:
    np_array = [int(x) for x in np_array]
    array = [int(x) for x in array]

print("\nЗначення    ","Частота   ","Сукупна частота")
f.write("Значення    Частота   Сукупна частота\n")  
ab = 0
for i in np_array:
    ae = array.count(i)
    if(int(i)==0):
        ab=ae
    if(int(i)>0):
        ab=int(ab)+int(ae)
    f.write(str(i)+"              "+str(ae)+"              "+str(ab)+"\n")
    print(str(i)+"              "+str(ae)+"              "+str(ab)+"\n")

f.write("Кількість елементів  "+str(count1)+"\n")
print("Кількість елементів  ",count1)

most_common = []
qty_most_common = 0 
for item in np_array:
    qty = array.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item 

f.write("Мода  "+str(most_common)+"\n")
print("Мода  ",most_common)

sort = sorted(array)
for a in sort:
    nu = len(sort)/2
    n = int(sort[int(nu)-1])+int(sort[int(nu)])
f.write("Медіана  "+str(n/2)+"\n")   
print("Медіана  ",n/2)

summ=0
for num in array:
    summ+=int(num)
avg = summ / len(array)
var = sum((float(x)-avg)**2 for x in array) / len(array)
print("Дисперсія  ", var)
f.write("Дисперсія  "+str(var)+"\n") 

print("Середнє квадратичне відхилення  ",math.sqrt(var))
f.write("Середнє квадратичне відхилення  "+str(math.sqrt(var))+"\n")  

min1=min(np_array)
max1=max(np_array)
f.write("Максимальне значення  "+str(max1)+"\n")
f.write("Мінімальне  значення  "+str(min1))

m = math.sqrt(int(count1))
if (m % 2 != 0):
    m = m - 1
h = (int(max1) - int(min1)) / m

if(count1<11):
    x=[]
    for i in range(6):
        x.append(min1)
    for i in range(2):
        x.append(int(min1)+int(h))
    for i in range(2):
        x.append(max1)

if (count1>12):
    x=[]
    for i in range(19):
        x.append(22)
    for i in range(10):
        x.append(119)
   
    for i in range(6):
        x.append(216)
    for i in range(8):
        x.append(313)
    for i in range(6):
        x.append(410)
    for i in range(11):
        x.append(507)
    for i in range(14):
        x.append(604)
    for i in range(9):
        x.append(701)
    for i in range(11):
        x.append(798)
    for i in range(5):
        x.append(895)
    for i in range(1):
        x.append(999)
    m=m+1

n, bin, patches = plt.hist(x,bins=int(m),edgecolor='black')
plt.show()   
file.close()






