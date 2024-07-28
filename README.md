#Text Encryption Using Caesar Cipher
This project is a Python-based graphical user interface (GUI) application that allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The application provides a straightforward method for applying one of the oldest known encryption techniques to secure messages. The GUI is designed to be user-friendly and intuitive, allowing users to easily input text and a shift value to perform encryption and decryption.

##Features
1.**Encrypt Text:** Users can input any text along with a numerical shift value. The application will encrypt the text by shifting each letter by the specified number of positions in the alphabet, wrapping around if necessary.
2.**Decrypt Text:** Users can also input encrypted text and the original shift value to decrypt the text, effectively reversing the encryption process to restore the original message.
3.**Error Handling:** The program includes error handling to manage non-integer shift inputs, ensuring robust user interactions with clear error messages.
4.**Sleek GUI:** The application features a modern interface with a black background and white text, designed to be easy on the eyes and straightforward to use.

##Technical Details
**Programming Language:** Python
**GUI Toolkit:** Tkinter
**Error Management:** Python's messagebox from Tkinter for user alerts
**Code Organization:** Modular design with separate functions for encryption, decryption, and GUI operations.

##How It Works
The Caesar Cipher algorithm shifts the letters of the alphabet by a set amount determined by the user. This simple, yet effective, method of encryption provides a basic level of security for messages. The GUI provides text boxes for user input and buttons to initiate encryption or decryption, displaying the result in the same window.

##Encryption Process
The text is taken from the user along with a shift value.
Each letter in the text is shifted forward in the alphabet by the amount specified in the shift value, wrapping around the alphabet if necessary.

##Decryption Process
The encrypted text is taken from the user along with the original shift value.
Each letter in the encrypted text is shifted backward by the shift value to restore the original text.
Getting Started
To run this application, ensure you have Python and Tkinter installed on your system. Clone this repository and run the script using:

bash
Copy code
python text_encryption_caesar_cipher.py
Dependencies
Python 3.x
Tkinter


Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.


