#!/usr/bin/env python

user = {'admin': True, 'active': True, 'name': 'Paul'}

if user ['admin'] and user ['active']:
    print('user is active')
elif user['admin']:
    print("(ADMIN) %s" % user['name'])
else:
   print(user['name'])
