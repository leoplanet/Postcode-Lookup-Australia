Postcode-Lookup-Australia
=========================

Python script to verify and look up Australian Postcode and Localities

This python script has been provided as an example to show how easy it is to use a csv file and query it. The intention of this script is not to facilitate the use of the AustPost data in any manner that the data owners do not allow. Please respect the wishes of the data owners and use the data for personal purposes only

Here is how to use the script:

run the script with 1, 2 or 3 arguments

1 argument
================================================================================
The first argument is the name of the csv file containing the postcode data.

./querypostcode.py pc-full_20131024.csv

This will load the file into a python dictionary and print the Postcodes as key and a list of Localities as value in the dictionary


2 arguments
================================================================================
The first argument is the name of the csv file containing the postcode data and the second argument is the postcode to look up.

./querypostcode.py pc-full_20131024.csv 2000

This will give you all the localities associated with that postcode. If the postcode does not exist in the data you will get a message "postcode not found"

3 arguments
================================================================================
The first argument is the name of the csv file containing the postcode data and the second argument is the postcode and the third argument shall be the locality

./querypostcode.py pc-full_20131024.csv 2000 sydney

This will compare if the postcode locality pair you have provided is correct. If the correct it will return 'True' otherwise 'False'.