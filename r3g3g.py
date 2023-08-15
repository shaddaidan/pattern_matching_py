# using regex
# you have to first import it in order to use it

import re

# for more information on hoe to use re check our re doc(hehe that is really cool)

phone_no = re.compile(r'\d{3}-\d{3}-\d{4}')

message = ' Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. '

mo = phone_no.search(message)

print('number found',  mo.group())

# now to try out more powerful functions.
# we would be getting the grouping of passed thingies now

phone_no0 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

mo0 = phone_no0.search(message)

print('first set of no:', mo0.group()) # if you want to get a list of all the group present use groups() the plural

# you can assign your .groups to a variable. e.g fish, name = mo.groups