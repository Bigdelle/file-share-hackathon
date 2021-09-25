"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Benjamin Bigdelle (brb227)
Date:   9/14/21
"""
import a1

orig = input('Enter original currency: ')
des = input('Enter desired currency: ')
amt = input('Enter original amount: ')

print('You can exchange ' + a1.before_space(a1.get_old(a1.query_website(orig, des, amt))) + ' ' + orig + ' for ' + a1.before_space(a1.get_new(a1.query_website(orig, des, amt))) + ' ' + des + '.')
