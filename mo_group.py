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
# so this regex object would work if (no) is present or not.


'''
 i guess this counts as a comment i would be using it for content
 comments while i would be using the other one as heading comments
 yeah from now on
'''

# #matching zero or more with the star

# the * represents the match zero or more, it means the group that precedes the star can occur any number of times in the text or not occur at all

mo3 = re.compile(r'cat(no)*fish')

reg2 = mo3.search('this is a catfish')

print(reg2.group())




# matching one or more with the plus +
'''
in this type of regex object for the object to be called 
it must occur atleast once or else it would not work 
we use the plus sign to indicate this

'''

mo4 = re.compile(r'cat(no)+man')

reg3 = mo4.search('this is a catman hope you find it')

print(reg3 == None)

# print(reg3.group())  this has a value of none and bring out an error when run


# matching specific repetitions with braces
'''we use braces to represent objects that occur a number of
times like (he){4} this would represent hehehehe

you can also use it to represent a range of numbers (3,5) 
this would represent the range 3 to 5 
you can also leave out the first or second number in the braces 
to represent the minimum or maximum unbounded {3,} or {,5}'''

mo5 = re.compile(r'(sha){3,5}')

reg4 = mo5.search('this is a shashashasha workd')

print(reg4.group())

# greedy and non-greedy matching

'''
  Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous brace example returns 'HaHaHaHaHa' instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.

Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.
'''

# the findall( method)