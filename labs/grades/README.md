# TEMPERATURE CONVERSION
## General information
Create a script that extracts a °F temperature from a phrase, converts it in °C, and then displays the original phrase with the temperature °C, properly formatted. 
The phrase should be like the following example:
"Temperature in Athens is: 69 °F"
Assume that the phrase has the format appearing above, so the temperature value is always the 5th 'word'
Your script should:
print the original phrase, 
extract the original temperature, 
convert the temperature into C degrees,
print the converted text as: "Temperature in Athens is: 20.56 °C".

Format the output so that:
the temperature in C is rounded to 2 decimals, 
the degrees symbol ° that appears before C is set with its ASCII code (176) - hint: use the chr() function

The program should work for any value in F degrees inside the original string - so after you write the script, change the value of degrees F in the original string and make sure that the program runs properly. Before you submit, change the value of the original text back to 69.

{% next %}

 
## Run your program to see if it compiles

```
python temperature.py
```
With the original phrase "Temperature in Athens is: 69 degrees F", the output should be
"Temperature in Athens is: 20.56 °C"

Edit the original phrase in the code so that it reads "Temperature in Athens is: 75 degrees F"
Run your code again, the output should be "Temperature in Athens is: 23.89 °C"

Edit once more the original phrase in the code so that it reads "Temperature in Athens is: 102 degrees F"
Run your code again, the output should be "Temperature in Athens is: 38.89 °C"

{% next %}
 
## Check your code, using the check tool
 
```
check50  mkotsovoulou/python/main/labs/temperature
```

## Check the styling of your code, using the style tool
 
```
style50 temperature.py
```

## Submit your work 

```
submit50  mkotsovoulou/python/main/labs/temperature
```

DONE!
 
