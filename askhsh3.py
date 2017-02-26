# -*- coding: utf-8 -*-
#Άσκηση 3
print 'Εισάγετε μια λίστα στοιχείων χωρίς κόμμα'
a=raw_input()
a=[int(x) for x in a]
print 'Η λίστα που δώσατε είναι:',a
c=len(a)
k=0
b=list(a)
for i in range(0,c):
    if a[i]!=0:
        b[k]=a[i]
        k=k+1
    i=i+1
for i in range(k,c):
    b[i]=0
s=0    
for i in range(0,c):
    if b[i]==0:
        s=s+1
if s!=0:
    print 'Η λίστα με τα μηδενικά στοιχεία στο τέλος είναι:',b
else:
    print 'Η λίστα παρέμεινε η ίδια:',b

