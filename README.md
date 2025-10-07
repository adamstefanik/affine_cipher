# Affine Cipher GUI

A simple Python application for encrypting and decrypting text using the affine cipher algorithm.  
The project features an easy-to-use graphical user interface (GUI) built with Tkinter, allowing users to input text, set cipher keys, and view results instantly.

## Files

- **affine_cypher.py** — contains the affine cipher logic and helper functions
- **gui.py** — provides the graphical interface for user interaction
- **main.py** — (optional) allows you to launch the GUI by running `python main.py`
- **requirements.txt** — lists required dependencies (standard Python and Tkinter)

## How to Run

1. Make sure you have Python 3 installed.
2. (If you are on Linux and get an error about Tkinter, install it via  
   `sudo apt install python3-tk`.)
3. Install requirements (optional, usually not needed for Tkinter):
   ```
   pip install -r requirements.txt
   ```
4. Start the GUI application:
   ```
   python gui.py
   ```
   alebo ak používaš main.py:
   ```
   python main.py
   ```

## Features

- Clean graphical user interface
- Input filtering (removes diacritics, replaces spaces, keeps numbers)
- Easy encrypt/decrypt with chosen keys
- Copy output to clipboard
- Clear input/output fields
- Alphabet and ciphered alphabet preview

## License

This project is intended for educational purposes.