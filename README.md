# Sales Control System

A lightweight **Python-based CLI application** designed to manage and track product sales. This project demonstrates modular programming by separating core logic from the user interface.

## 🚀 Features

* **Interactive Menu**: Simple terminal-based navigation to add sales or exit the system.
* **Automated Calculations**: Automatically computes the total for each entry ($Quantity \times Unit Price$).
* **Sales History**: Displays a formatted summary of all transactions processed during the session.
* **Total Accumulation**: Provides a final sum of all revenue generated across all entries.

## 🛠️ Project Structure

* `main.py`: The entry point of the application containing the menu loop and reporting logic.
* `registrar.py`: Handles data input, dictionary creation, and the global sales list.

## 💻 How to Run

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/sales-control-system.git](https://github.com/your-username/sales-control-system.git)
    ```
2.  **Navigate to the folder**:
    ```bash
    cd sales-control-system
    ```
3.  **Execute the script**:
    ```bash
    python3 main.py
    ```

## 📝 Usage Example

```text
--- MENU ---
1. Add sale 
2. Exit system

Select Option: 1
What is the product name: Laptop
What is the product unit price: 800
What is the quantity sold: 2

PRODUCT Laptop --- QUANTITY SOLD 2 --- TOTAL $1600.0