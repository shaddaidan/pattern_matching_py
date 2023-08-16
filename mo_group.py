# we can find matching groups with pipe
# the | character is called a pipe

# so you can use it to match more than one regualr expression as shown below

import re


reg = re.compile (r'bat|super')

mo1 = reg.search('batman is so cool but superman is a lot cooler if you ask me')

# using search will only return the first occurence 
# but using the findall will return all occurences
# we would use this later on

print(mo1.group())

# now using pipe to match several patterns as part of regex.
#  we use the () for mathcing groups

reg0 = re.compile(r'super(man|dog|cat|girl)')
mo2 = reg0.search("everyone knows supercat is the coolest, second is super girl then superdog then all the other things in betwween like iono lois lane ")
print(mo2.group())

# adding numbers to your group you can specify what part of the text you want returned
# each () represents a group (food)(reg) 

# for optional matching you use question mark ?

reg1 = re.compile(r'super(no)?man') # hence the group that preceeds that mark is flagged as optional

# when we get back from work we would continue from here