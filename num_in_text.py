# this is check for a phone number in a line og text.
# so we have to do something cool here which would be to use a function we defined in another file
# in a different file yess.

from is_phone_number import is_phone_number

message = ' Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. '

for i in range(len(message)):
    if is_phone_number(message[i:i+12]):
        print('phone number found', message[i:i+12])
    

