# trying to achieve the same thing as the code above but this time using line split instead of but 14 characters at a time



from is_phone_number import is_phone_number

message = ' Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. '

split = message.strip()   # i cannot remember how to strip words and not characters at the moment so i would have to put a halt to this for the time being

for split in message:
    print(split)