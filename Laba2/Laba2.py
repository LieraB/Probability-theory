import numpy as np
import math
import matplotlib.pyplot as plt
import stemgraphic

print("Введіть назву файла")
name_file=input()
arr_num = np.loadtxt(r"C:\Users\babam\Pictures\\"+name_file+".txt", delimiter='\t')

sort_arr=sorted(arr_num)
N=len(sort_arr)
q1=1/4*(N+1)
x=q1-int(q1)
Q1=sort_arr[int(q1)-1]+x*(sort_arr[int(q1)]-sort_arr[int(q1)-1])
print("Q1=",Q1)

q3=3/4*(N+1)
x3=q3-int(q3)
Q3=sort_arr[int(q3)-1]+x3*(sort_arr[int(q3)]-sort_arr[int(q3)-1])
print("Q3=",Q3)

x4=(90/100)*(N+1)
x5=x4-int(x4)
print("P90=",sort_arr[int(x4)-1]+x5*(sort_arr[int(x4)]-sort_arr[int(x4)-1]))

avg = sum(arr_num)/N
var = sum((float(x)-avg)**2 for x in arr_num) / N
print("Стандартне відхилення  ",math.sqrt(var))

var1=sum(abs(int(x)-avg) for x in arr_num) / N
print("Середнє відхилення  ", var1)

M1 = np.array([[100., 1.], [avg, 1.]])
v1 = np.array([100., 95.])
y=np.linalg.solve(M1, v1)
new_arr=[]
for i in arr_num:
    new_arr.append(y[0]*i+y[1])
new_arr = [int(numeric_string) for numeric_string in new_arr]
print("Нові значення   ",np.sort(new_arr))

stemgraphic.stem_graphic (sort_arr, scale = 10)
plt.show()
plt.boxplot(sort_arr)
plt.show()


