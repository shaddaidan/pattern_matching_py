# REGEXES

Regular expressions, called regexes for short,  are descriptions for a pattern of text.

Regular expressions, called regexes for short, are descriptions for a pattern of text. For example, a \d in a regex stands for a digit character—that is, any single numeral from 0 to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text pattern the previous isPhoneNumber() function did: a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. Any other string would not match the \d\d\d-\d\d\d-\d\d\d\d regex.

## CREATING REGEX OBJECTS

All the regex functions in Python are in the re module. Enter the following into the interactive shell to import this module:
>import re

The mo variable name is just a generic name to use for Match objects

## REVEIW OF REGULAR EXPRESSION MATCHING

> While there are several steps to using regular expressions in Python, each step is fairly simple.
> 1. Import the regex module with import re.
> 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
> 3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
> 4. Call the Match object’s group() method to return a string of the actual matched text.

### NOTES
While I encourage you to enter the example code into the interactive shell, you should also make use of web-based regular expression testers, which can show you exactly how a regex matches a piece of text that you enter. I recommend the tester at https://pythex.org/.

## Grouping with Parentheses

Say you want to separate the area code from the rest of the phone number. Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d). Then you can use the group() match object method to grab the matching text from just one group.

The first set of parentheses in a regex string will be group 1. The second set will be group 2. By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text. Enter the following into the interactive shell: