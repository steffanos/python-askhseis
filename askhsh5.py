# -*- coding: utf-8 -*-
#Άσκηση 5
l1=[]
for i in range(101):
    a=i%10
    b=i//10
    s=a+b
    if s!=0:
        if i%s==0:
            l1.append(i)
for i in range(101,1001):
    a=i//100
    b=i%100//10
    c=i%100%10
    s=a+b+c
    if s!=0:
        if i%s==0:
            l1.append(i)
print 'Οι αριθμοί Harshad μέχρι το 1000 είναι:',l1
l2=[]
for i in range(1,10):
    l2.append(i)
for i in range(10,101):
    f=i%10
    g=i//10
    h=f*g
    if h!=0:
        if i%h==0:
            l2.append(i)
for i in range(101,1001):
    f=i//100
    g=i%100//10
    j=i%100%10
    h=f*g*j
    if h!=0:
        if i%h==0:
            l2.append(i)
print 'Οι αριθμοί που το γινόμενο των ψηφίων τους διαιρεί τον ίδιο τον αριθμό είναι:',l2            
