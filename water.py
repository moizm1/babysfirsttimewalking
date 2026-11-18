#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define the variables for every listed property in the table.
cas_number = "7732-18-5"
rho = 1000
mu = 1
Tm = 273.15
Tb = 373.13
k = 0.58

# Define the functions 

def convert_to_kelvin(temperature, units):
    """ (int or float, str) -> float

    Converts a given temperature to Kelvin based on the provided unit and returns its value.
    The function returns None for any invalid input type. 

    >>> convert_to_kelvin(90, "C")
    263.15
    >>> convert_to_kelvin(32.0, "F")
    273.15
    >>> convert_to_kelvin("32.0", "F")
    None

    """
    #make sure that the arguments are the correct type
    if type(temperature) not in (int, float):
        return None
    if type(units) != str or len(units) != 1:
        return None

    #clean up any whitespace or incorrect case in the given units then make sure the units given are farenheit, celcius or kelvin
    clean_units = units.strip().upper()
    if clean_units not in ("C", "F", "K"):
        return None

    #convert farenheit to celsius
    if clean_units == "F":
        clean_units = "C"
        temperature = (temperature - 32) * 5 / 9

    #convert celsius to kelvin
    if clean_units == "C":
        temperature += 273.15

    return float(temperature)


def is_gas(temperature):
    """ (float or int) -> (bool)

    Returns True if water is gas at the specified temperature (in Kelvin), False otherwise. 
    The function returns None for any invalid input type. 

    >>> is_gas(270)
    False
    >>> is_gas(400)
    True
    >>> is_gas("")
    None 
    """
    #make sure the input is a numerical value
    if type(temperature) not in (int, float):
        return None

    #check if the temperature in kelvin is greater than the boiling point
    if temperature > Tb:
        return True
    else:
        return False

def is_liquid(temperature):
    """ (float or int) -> (bool)

    Returns True if water is liquid at the specified temperature (in Kelvin), False otherwise. 
    The function returns None for any invalid input type. 

    >>> is_liquid(270)
    False
    >>> is_liquid(350)
    True
    >>> is_liquid("325.0")
    None 
    """
    #make sure the input is a numerical value
    if type(temperature) not in (int, float):
        return None

    #check if the temperature in kelvin is between the melting and boiling point
    if Tm <= temperature <= Tb:
        return True
    else:
        return False

def is_solid(temperature):
    """ (float or int) -> (bool)

    Returns True if water is solid at the specified temperature (in Kelvin), False otherwise. 
    The function returns None for any invalid input type. 

    >>> is_solid(270)
    True
    >>> is_solid(350)
    False
    >>> is_solid([230])
    None 
    """
    #make sure the input is a numerical value
    if type(temperature) not in (int, float):
        return None

    #check if the temperature in kelvin is less than the melting point
    if temperature < Tm:
        return True
    else:
        return False

# develop the module such that if (and only if) it is executed as a script, 
# it does the listed tasks in the problem statment.

if __name__ == "__main__":

    #queries the user for units
    units = input("What are the units for temeprature, C/F/K: ")

    #queries the user for temperature value
    temperature = float(input("What is the temperature value: "))

    #defines the kelvin temperature
    kelvin_temp = convert_to_kelvin(temperature, units)

    if kelvin_temp == None:
        print("Invalid input!")
    elif is_gas(kelvin_temp):
        print("gas")
    elif is_liquid(kelvin_temp):
        print("liquid")
    else:
        print("solid")


