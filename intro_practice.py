import pandas as pd 
import numpy as np

# Creating a number variable 
var_number = 10 

# Creating a string variable 
var_string = "Hello"

# Creating a list
list_example = [1,2,3,4,5]

# Creating a dictionary with at least 3 key value pairs
dictionary_example = {
    "name": "Amen", 
    "age": 24, 
    "job": "scribe", 
    "address": {
        "city": "new_rochelle", 
        "state": "NY",
        "country": "united_states",
    }
}

# Create a function that takes in at least two inputs (otherwise called variables or arguments) and write some a calculation that involves a if/else statement 
def analyze_weather(temperature, humidity):
    # Print the input values
    print("Temperature:", temperature)
    print("Humidity:", humidity)

    # If/Else statement to determine if the weather is comfortable
    if temperature >= 60 and temperature <= 75 and humidity < 60:
        weather_status = "Comfortable"
    else:
        weather_status = "Uncomfortable"

    # Print the output of the function
    print("Weather Analysis:", weather_status)

    # Return the weather status
    return weather_status
# Example data
temp = 70
humid = 50

# Call the function with the example data
weather_result = analyze_weather(temp, humid)

# Print the output
print("Weather Analysis Result:", weather_result)
