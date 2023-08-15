car = '45'
house = '345'
mathew = 'mathew'

# print(car.isdecimal())
# print(house.isdecimal())
# print(mathew.isdecimal())

def decimal(val):
    if val.isdecimal():
        return True
    
    else :
        return False
    
print(decimal(car))
print(decimal(house))
print(decimal(mathew))