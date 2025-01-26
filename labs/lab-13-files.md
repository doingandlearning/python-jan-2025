# Lab 13: Files

The aim of this lab is to work with the `csv` module to load data from a CSV file.

We will add a feature to your application that allows the program to load data from a file, rather than requiring the user to enter values or hard-coding those values in the program.

This lab is comprised of 6 steps:
1. Create the `loader.py` module
2. Create the data file
3. Prompt the user for the filename to load
4. Load the data file
5. Invoke the `load_data` function
6. Rerun your application

## Step 1: Create the `loader.py` Module

Create a new file to define a load function in.

To do this, add a new module/file to your application called `loader.py`.

At the start of the file, add the required imports, for example:

```python
import csv
from readings import TemperatureReading
```

Note that `csv` is a built-in module available with Python.

## Step 2: Create the Data File

The data will be saved in CSV format in a file called `data.csv`.

Each row in the file will contain 4 values separated by commas.

The values will represent:

- Temperature
- Scale
- Date
- Location

An example of the contents of the file is given below:

```
13.5,Celsius,01/05/20,London
12.6,Celsius,02/05/20,London
15.3,Celsius,03/05/20,London
12.2,Celsius,04/05/20,London
16.6,Celsius,05/05/20,London
14.6,Celsius,06/05/20,London
15.6,Celsius,07/05/20,London
```

Save this data into a file in the same directory as your program.

## Step 3: Prompt the User for the Filename to Load

The program should ask the user for the name of the file to load. You can allow the user to press Enter to use a default filename (such as `data.csv`). For example:

```python
filename = input('Please enter the data file to load (data.csv): ')
if filename == '':
    filename = 'data.csv'
```

## Step 4: Load the Data File

Write a function to load the data from a CSV file. To do this, write a function called `load_data()` in the `loader.py` module.

The `load_data()` function should take the name of the file to load.

It should then use the `csv` library to load data from a CSV file into a list container type.

To do this, you should use the `with as` construct when opening the file. You can then use the `csv.reader()` function to read the contents of the file into a reader object. You can then loop through each row in turn in the reader.

Each row should contain 4 items of information. If a row does not contain 4 items of information, then you should log this for the user to investigate at a later stage.

When you load a row, you should use it to create a new instance of the `TemperatureReading` class, for example:

```python
temp = float(row[0])
scale = row[1]
date = row[2]
location = row[3]
reading = TemperatureReading(temp, date, location, scale)
```

The `load_data()` function should return a list containing instances representing the rows in the CSV file.

## Step 5: Invoke the `load_data` Function

In your main application program, you should modify the code so that the `readings` list is populated with data returned from the `load_data()` function. For example:

```python
# Load the data file
readings = load_data(filename)
```

## Step 6: Rerun Your Application

Your program should now load the data from the CSV file; however, all other functionalities should work as before.

The output from the sample solution program for the CSV file given above is shown below:

```
Please enter the data file to load (data.csv): 
Loading file data.csv
Finished reading file
All Temperature Readings:
TemperatureReading[Celsius](13.5 on 01/05/20 at London) 
TemperatureReading[Celsius](12.6 on 02/05/20 at London) 
TemperatureReading[Celsius](15.3 on 03/05/20 at London) 
TemperatureReading[Celsius](12.2 on 04/05/20 at London) 
TemperatureReading[Celsius](16.6 on 05/05/20 at London) 
TemperatureReading[Celsius](14.6 on 06/05/20 at London) 
TemperatureReading[Celsius](15.6 on 07/05/20 at London)
Fahrenheit Temperatures: [56.3, 54.68, 59.540000000000006, 53.96, 61.88, 58.28, 60.08]
Temperatures: [13.5, 12.6, 15.3, 12.2, 16.6, 14.6, 15.6]
Dates: ['01/05/20', '02/05/20', '03/05/20', '04/05/20', '05/05/20', '06/05/20', '07/05/20']
Temperatures above 14.0: [<readings.TemperatureReading object at 0x10b9beeb0>, <readings.TemperatureReading object at 0x10b9bed30>, <readings.TemperatureReading object at 0x10b9a8a90>, <readings.TemperatureReading object at 0x10b9a8af0>]
Min temp in list = TemperatureReading[Celsius](12.2 on 04/05/20 at London)
Max temp in list = TemperatureReading[Celsius](16.6 on 05/05/20 at London)
Average temperature = 14.34
Median temperature value = TemperatureReading[Celsius](14.6 on 06/05/20 at London)
Range of temperatures from 12.2 to 16.6
Add two temperatures TemperatureReading[Celsius](29.0 on 01/05/20 at London)
Add a temperature and an int TemperatureReading[Celsius](18.5 on 01/05/20 at London)
Add a temperature and a float TemperatureReading[Celsius](19.0 on 01/05/20 at London)
All Rainfall Readings:
RainfallReading[11:00](2.0 on 01/05/20 at London) 
RainfallReading[11:30](2.6 on 02/05/20 at London) 
RainfallReading[11:00](2.3 on 03/05/20 at London) 
RainfallReading[12:00](3.2 on 04/05/20 at London) 
RainfallReading[10:45](1.6 on 05/05/20 at London)
Average rainfall 2.34
InvalidTemperatureException(5.5, Invalid type for addition to TemperatureReading)
Done
```

---