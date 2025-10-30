# Modern & Safe Python Calculator

This is a sleek, modern, and secure desktop calculator built with Python. It uses **CustomTkinter** for a beautiful, theme-aware user interface and Python's built-in **`ast` (Abstract Syntax Trees)** module to safely evaluate mathematical expressions without using the dangerous `eval()` function.

## ✨ Features

* **Modern UI:** Built with `customtkinter` for a beautiful look that supports both dark and light modes.
* **Safe by Design:** Uses `ast` parsing instead of `eval()`. This means it only evaluates mathematical operations and **cannot execute arbitrary or malicious code**.
* **Correct Order of Operations:** Accurately handles complex expressions, including parentheses (e.g., `5 * (10 + 2)`).
* **Standard Operations:** Includes all essential functions:
    * Addition (`+`)
    * Subtraction (`-`)
    * Multiplication (`*`)
    * Division (`/`)
* **Utility Buttons:** Features 'C' for a full clear and '<-' for backspace.

## 🚀 The "Safe & Cool" Part: Why `ast`?

Many simple Python calculators use the `eval()` function for convenience. However, `eval()` is a major security risk because it can execute *any* Python code passed to it.

This project takes a more robust and secure approach:

1.  **Parse, Don't Evaluate:** It uses `ast.parse()` to convert the input string (e.g., "5 + 3") into an Abstract Syntax Tree—a tree-like structure representing the code's components.
2.  **Whitelist Operations:** A custom `SafeCalculator` class recursively "walks" this tree.
3.  **Execute Safely:** It *only* performs operations from a pre-approved "whitelist" (like `ast.Add`, `ast.Sub`, `ast.Mult`, etc.) and *only* on numeric values. Any other node type (like function calls, imports, or variable names) is rejected with an error.

This method gives us the power of a real parser while maintaining complete control and security.

## 🛠️ Installation & Usage

To run this calculator, you'll need Python 3 and the `customtkinter` library.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the required library:**
    ```bash
    pip install customtkinter
    ```
    *(Or `pip3 install customtkinter` depending on your setup)*

3.  **Run the application:**
    ```bash
    python calculator.py
    ```
    *(Assuming you named your file `calculator.py`)*

## 💻 Technologies Used

* **Python 3**
* **CustomTkinter:** For the modern GUI framework.
* **`ast` Module (built-in):** For safe expression parsing.
* **`operator` Module (built-in):** For handling the mathematical operations.
