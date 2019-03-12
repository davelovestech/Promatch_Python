#!/usr/bin/env python3

sale = True

if sale:
        print('time to buy')
else:
        print('wait for sale')


age = 88

if age <= 0:
        print('You have not even seen the light at all')
elif 0 < age <= 16:
        print('You can\'t drive yet')

elif 16 < age < 80:
        print('You can drive')

else:
        print('You need a chauffeur')
