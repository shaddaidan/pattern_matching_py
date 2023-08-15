# making a function that checks to see if i line is a phone number or not.
# first it takes in the line of codes 
# if the line is a number then it would return true if it is not then it would return false
# if the first 3 characterss are not decimals then it would return false
# if the fourth character is not a hyphen (-) return false
# and you continue like that till you have runned the entire line of the code 
# when you have ran through the entire code retun true


def is_phone_number(value):
    if len(value) != 12:
        return False
    
    for i in range(0,3):
        if not value[i].isdecimal():
            return False
        
    if value[3] != '-':
        return False
    
    for i in range(4, 7):
       if not value[i].isdecimal():
            return False
    if value[7] != '-':
        return False
    for i in range(8, 12):
        if not value[i].isdecimal():
            return False
    return True


        
    