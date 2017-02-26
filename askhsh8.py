# -*- coding: utf-8 -*-
#Άσκηση 8
import tweepy
from tweepy import OAuthHandler
consumer_key = 'JabRkANKtCxW5s5ziioIiKQsC'
consumer_secret = 'MqSJDwXyF3TwxwP5dM92rMol4sqolNSGvONvfHeIfldqnMXBI6'
access_token = '816641005143420928-RTm4pMJR2x8ix9MAsoBAvtzOU12moDe'
access_secret = '3SNYJF8NAor0GMhA3Hse24LjdG3o6wq3agjcfEs61sBRx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print'Εισάγετε το username του πρώτου χρήστη του twitter'
user1=(str(input('username:')))
print'Εισάγετε το username του δεύτερου χρήστη του twitter'
user2=(str(input('username:')))
x=api.get_user(user1)
z=api.get_user(user2)
print'Το όνομα του πρώτου χρήστη είναι:',x.name
print'Το όνομα του δεύτερου χρήστη είναι:',z.name
l1=[]
for i in api.followers_ids(user1):
    l1.append(api.get_user(i).screen_name)
l2=[]
for j in api.followers_ids(user2):
    l2.append(api.get_user(j).screen_name)
k=0
for e in set(l1) & set(l2):
    k=k+1
if (k>0):
    print'Οι κοινοί followers είναι:'
    for e in set(l1) & set(l2):
        print api.get_user(e).screen_name
else:
    print'Δεν υπάρχουν κοινοί followers'

