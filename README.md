# TSHTestDataConversion_Lennox20190214
BME 547 Assignment: TSH Test Data Conversion

This program loads information from the data file test_data.txt. It reads the information for each individual patient into the categories first name, last name, age, gender, and TSH values. These values are stored in the class Person so they can be manipulated in future operations. 

The TSH values are an array of numbers that are converted into floating points by the program. They are then sorted into numerical order. The TSH values are then used to diagnose the patient as having hypothyroidism, hyperthyroidism, or normal thyroid function based on the following TSH values:

Hyperthyroidism: TSH < 1.0
Hypothyroidism: TSH > 4.0
Normal thyroid function: Otherwise

The diagnosis, along with all other variables inside the class Person are then stored in a dictionary and written to a .json file with the name FirstName-LastName.json.

No inputs are required of the user. However, test_data.txt does need to be in the same file location as the program for this to work.
