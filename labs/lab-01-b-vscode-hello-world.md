# Lab 1: Hello World (Using VS Code)

The aim of this lab is to create a simple Python application to print out a welcome message using Visual Studio Code (VS Code).

The application should follow the same format as that presented in the lecture, and we'll use VS Code for this lab.

This lab is made up of the following steps:
1. Getting VS Code running
2. Creating an application
3. Running the application
4. Expanding the application

## Step 1: Start up Visual Studio Code

Start up Visual Studio Code.

If this is your first time using VS Code, you may see a "Welcome" screen. You can close this screen if you'd like.

Now, let's open a new folder for your project:
1. Click on `File` > `Open Folder...`.
2. Choose a location on your computer where you want to create your project and create a new folder (e.g., `HelloWorldProject`).
3. Select the newly created folder and click `Open`.

You should now see your new project folder in the Explorer view on the left side of the VS Code window.

## Step 2: Set up the Python Environment

Before writing any Python code, you'll need to set up the Python environment.

1. If you haven't installed the Python extension for VS Code, you'll be prompted to install it. Follow the prompt and install the extension.
   - If you don’t see the prompt, you can manually install the extension:
     - Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window or pressing `Ctrl+Shift+X`.
     - Search for "Python" and install the official Python extension by Microsoft.

2. Set up a virtual environment for your project:
   - Open the terminal in VS Code by selecting `Terminal` > `New Terminal`.
   - Create a virtual environment in your project folder by running the following command:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. Select the Python interpreter for your project:
   - In VS Code, open the Command Palette by pressing `Ctrl+Shift+P`.
   - Type `Python: Select Interpreter` and select the interpreter from your virtual environment (it should show something like `.venv` followed by the Python version).

## Step 3: Create an Application

Now, let's create the Python application.

1. In the Explorer view, click on the `New File` icon next to your project folder name and name the new file `main.py`.

2. Open `main.py` and add the following code:
   ```python
   print('Hello World!')
   ```

3. Save the file by clicking `File` > `Save` or pressing `Ctrl+S`.

## Step 4: Run the Application

To run the Python application:

1. Ensure that your terminal is still open and that your virtual environment is active.
2. Run the Python script by typing the following command in the terminal:
   ```bash
   python main.py
   ```

3. You should see the output in the terminal:
   ```
   Hello World!
   ```

## Step 5: Add Further Code

Let's extend the functionality of your application.

1. Modify your program to print the result of adding 2 and 3 together. Add the following code to `main.py`:
   ```python
   print(2 + 3)
   ```

2. Save the file and rerun the program by executing the following command in the terminal:
   ```bash
   python main.py
   ```

3. The output should now look like this:
   ```
   Hello World!
   5
   ```

4. Finally, add the following line at the end of your program:
   ```python
   print('-' * 25)
   ```

5. Save the file and rerun the program. The final output should be:
   ```
   Hello World!
   5
   -------------------------
   ```

## Conclusion

You've now successfully created and run a simple Python application using Visual Studio Code. You've learned how to set up a Python project in VS Code, how to use a virtual environment, and how to write and execute Python code.

---

## Questions?

If you have any questions, feel free to ask!
