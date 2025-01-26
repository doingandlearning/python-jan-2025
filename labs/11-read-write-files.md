# Lab 11: File Access

The aim of this lab is to explore creating and accessing the contents of a file.

---

## Objective

Write a program to:

1. Create a file and write today's date into it. 
   - The file name can be hard-coded or supplied by the user.
   - Use `datetime.today()` to get the current date and time.
   - Use `str()` to convert the datetime object into a string to write it to the file.

2. Example template to get started:

   ```python
   from datetime import datetime

   print('Creating file')

   with open('date_file.txt', 'w') as file:
       print('Writing date information to file')
       # Your code goes here

   print('Done')
   ```

3. Verify the contents of the newly created file using an editor (e.g., PyCharm) to open the file.

---

## Extension Point

As an extension, write a second program to:

1. Reload the date from the file and convert the string back into a date object.
2. Use `datetime.strptime()` to convert the string into a datetime object. Documentation on this function can be found [here](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime).
   - This function requires a date string and a format string that defines the expected format.
   - Assuming you used the approach in step 1, the following format should work to parse the date string and create a datetime object:

   ```python
   datetime_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
   ```
