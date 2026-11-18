#!/usr/bin/env python
# coding: utf-8

# In[41]:


def to_celsius(temperature, unit):
    '''
    (int/float, string) --> (int/float)

    A function that converts (or preserves) an input tempreature, farenheit or celsius, to celsius. Returns a number which reperesents the tempreature in celsius.

    - tempreature: A number (int of float)
    - unit: a string, either "C" for celsius or "F" for farenheit (either upper of lowercase)

        >>> to_celsius(10, "C")
        10
        >>> to_celsius(40, "f")
        4.444444444444445
    '''
    #normalize the unit string
    clean_unit = unit.strip().lower()

    #determine the temperature in celsius, depending on the unit of input temperature
    if clean_unit == "c":
        celsius_temp = temperature
    elif clean_unit == "f":
        celsius_temp = (temperature - 32)*(5/9)
    else:
        print(unit, "is not a valid temperature unit")
        return None

    return celsius_temp

#print(to_celsius(10, "C"))
#print(to_celsius(40, "f"))


# In[54]:


def needs_jacket(temperature, unit, is_raining):
    '''
    (int/float, string, boolean) --> boolean

    A function that evaluates the weather conditions, temrpeature and rain, and returns a boolean value to determine if a jacket is needed.

    - temperature: A number (int or float)
    - unit: a string, either "C" for celsius or "F" for Fahrenheit (either upper or lowercase)
    - is_raining: a boolean, True if its is raining or otherwise false

        >>> needs_jacket(10, "C", False)
        False
        >>> needs_jacket(64, "f", True)
        True
        >>> needs_jacket(72.0, "F", True)
        False
    '''
    #Call the celsius conversion function to get the local temperature in celsius
    celsius_temp = to_celsius(temperature, unit)

    #Handle incorrect units
    if celsius_temp is None:
        return None

    #Determine if a jacket is needed or not
    if celsius_temp < 15 or (is_raining == True and celsius_temp < 22):
        return True
    else:
        return False

#needs_jacket(10, "C", False)
#needs_jacket(18, "C", True)
#needs_jacket(18, "C", False)
#needs_jacket(25, "C", True)
#needs_jacket(50, "F", False)
#needs_jacket(64, "f", False)
#needs_jacket(64, "F", True)
#needs_jacket(59, "F", False)
#needs_jacket(72, "F", True)


# In[53]:


def jacket_message(temperature, unit, is_raining):
    '''
    (int/float, string, boolean) --> boolean

    A function that evaluates the weather conditions, temrpeature and rain, and returns a string giving advice for clothing and carrying an umbrella.

    - temperature: A number (int or float)
    - unit: a string, either "C" for celsius or "F" for Fahrenheit (either upper or lowercase)
    - is_raining: a boolean, True if its is raining or otherwise false

        >>> jacket_message(-5, "C", False)
        "Wear a winter coat."
        >>> jacket_message(23, "f", False)
        "Wear a winter coat."
        >>> jacket_message(10, "C", True)
        "Bring a jacket. Don't forget an umbrella."
    '''
    #Call the celsius conversion function to get the local temperature in celsius
    celsius_temp = to_celsius(temperature, unit)

    #Handle invalid units
    if celsius_temp is None:
        return None

    #Determine what piece of clothing is recommended based off the temperature and needs_jacket function
    if celsius_temp < 0:
        clothing_advice = "Wear a winter coat."
    elif needs_jacket(temperature, unit, is_raining):
        clothing_advice = "Bring a jacket."
    else:
        clothing_advice = "No jacket needed."

    #Determine if an umbrella is needed
    if is_raining == True:
        advice = clothing_advice + " Don't forget to bring an umbrella."
    else:
        advice = clothing_advice

    return advice

#jacket_message(-5, "C", True)
#jacket_message(23, "F", False)
#jacket_message(0, "C", False)
#jacket_message(10, "C", True)
#jacket_message(18, "C", False)
#jacket_message(25, "C", True)
#jacket_message(-3, "c", True)


# In[ ]:


#Gather inputs from the user and convert to correct object types as needed
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ")
is_raining_string = input("Is it raining (yes/no): ")

#Clean up the rain input
clean_is_raining_string = is_raining_string.strip().lower()
#Convert the rain response into a boolean value
if clean_is_raining_string == "yes":
    is_raining = True
else:
    is_raining = False

#Print the weather data and display the advice to the user using the functions
print("Temperature in celsius: " + str(round(to_celsius(temperature, unit), 1)))
print("Bring a jacket: " + str(needs_jacket(temperature, unit, is_raining)))
print("Advice: " + jacket_message(temperature, unit, is_raining))


# In[ ]:




