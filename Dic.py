import random
import pprint
n=0
even = []
odd = []
while n < 100:
    f = random.randint(1,100)
    if f % 2 == 0:
        even.append(f)
    else:
        odd.append(f)
    n += 1
sum_even = [sum(even)]
sum_odd = [sum(odd)]
print(sum_odd) #проверка логики
total = {}
t = 1
for variable in even, odd, sum_even, sum_odd:
    total[t]=variable
    t+=1
pprint.pprint(total, width=1)
