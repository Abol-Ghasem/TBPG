# TBPG - Time-Based Password Generator

## Introduction  
TBPG is a **time-based password generator** that creates unique passwords using either the **current date and time** or a **user-specified date**. It's a simple, fast, and efficient tool for generating dynamic and secure passwords.

## Features  
- **Generate passwords** based on the **current date and time**  
- **Generate passwords** using a **user-specified date**  
- **Save generated passwords** to a file (`TBPG.txt`)  
- **Colorful and interactive CLI interface**  
- **Automatic dependency installation** on first run  

## Installation & Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/Abol-Ghasem/TBPG
cd TBPG
```

### 2. Run the Program  
Simply run:  
```bash
python main.py
```
Dependencies will be installed automatically on the first run.

## Dependencies  
This project requires the **TBPG** package. If necessary, you can install it manually:  
```bash
pip install TBPG
```

## How to Use  
Once the program starts, the following menu will appear:

```
----------------------------------------
 ______  ____   ____    ____ 
|      T|    \ |    \  /    T
|      ||  o  )|  o  )Y   __j
l_j  l_j|     T|   _/ |  T  
  |  |  |  O  ||  |   |  l_ |
  |  |  |     ||  |   |     |
  l__j  l_____jl__j   l___,_j
----------------------------------------
| 1. Generate password using current date |
----------------------------------------
| 2. Generate password using a specific date |
----------------------------------------
| 3. Exit                                 |
----------------------------------------
```

### Menu Options:  
- **1**: Generate a password using the current date and time.  
- **2**: Enter a specific date to generate a password.  
- **3**: Exit the program.  

## Saving Passwords  
If the user chooses to save the generated password, it will be stored in the `TBPG.txt` file.  

## Date Input Format  
For option **2**, enter the date in the following format:  
```
YYYY-MM-DD HH:MM:SS
```
Example:  
```
2025-01-28 17:29:13
```

## Contribution  
If you have any ideas for improving this project, feel free to share your feedback! You can also contribute by forking the repository and submitting a pull request.  
