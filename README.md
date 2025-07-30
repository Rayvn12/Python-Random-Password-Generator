Random Password Generator
Overview
This project is a Python-based Random Password Generator that allows users to create secure passwords based on custom preferences. The program supports different character types and ensures each password meets basic complexity requirements.

Features
User-defined password length (minimum of 6 characters)

Option to include:

Lowercase letters

Uppercase letters

Numbers

Symbols

Ensures at least one character from each selected category

Randomized character selection and final password shuffling

Input validation and error handling

Optional bonus features include:

Generating multiple passwords in one session

Copying passwords to the clipboard using the pyperclip module

How It Works
The user enters the desired password length

The user selects which types of characters to include

The program verifies the input and generates a password using characters from the selected sets

The password is displayed in the terminal

Getting Started
Prerequisites
Python 3.x

(Optional) pyperclip module if using the copy-to-clipboard feature

To install pyperclip, run:

nginx
Copy
Edit
pip install pyperclip
How to Run
Save the script as password_generator.py

Open your terminal or command prompt

Navigate to the folder containing the script

Run the program with:

nginx
Copy
Edit
python password_generator.py
Example Output
pgsql
Copy
Edit
Enter desired password length: 10
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated Password: Tr9mLp6kQe
File Structure
password_generator.py — Main script for the password generator

Future Enhancements
Add a graphical user interface (GUI) using Tkinter

Include password strength ratings

Add an option to store generated passwords securely

License
This project is intended for educational use and personal learning.
