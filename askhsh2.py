# -*- coding: utf-8 -*-
#Άσκηση 2
x=str(input('Εισάγετε μια ακολουθία παρενθέσεων μέσα σε εισαγωγικά:'))
a=len(x)
l=[]
l=x
k=0
s=0
n=0
for i in range(0,a):
    if(l[a-1]=='('):
        k=0
    else:    
        if(l[i]=='(' and l[i+1]==')'):
                    k=k+1
    if(l[i]=='('):
        s=s+1
    if(l[i]==')'):
        n=n+1
if(s==n and k>0):
    print 'True'
else:
    print 'False'























