# Sales Control System (GUI Version)

A **Python-based Desktop Application** built with **Tkinter** to manage and track product sales through a unified graphical interface. This project demonstrates modular programming and real-time data validation in a desktop environment.

## 🚀 Features

* **Unified Graphical Interface**: All operations occur in a single persistent window, eliminating disruptive pop-up dialogs.
* **Real-Time Sales History**: Features a dynamic table that displays each transaction (Product, Quantity, and Total) as it is registered.
* **Automatic Input Validation**: The system includes built-in checks to ensure product names are provided and that prices/quantities are valid positive numbers.
* **Automated Calculations**: Instantly computes the total for each entry ($Quantity \times Unit Price$) and maintains a running accumulated total for the entire session.

## 🛠️ Project Structure

* **`main.py`**: The entry point that initializes the Tkinter root window and launches the application loop.
* **`registrar.py`**: Contains the core `SalesApp` class, managing the interface layout, sales logic, and data validation.

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

## 📝 Usage Guide

1.  **Enter Details**: Type the product name, unit price, and quantity into the provided text boxes.
2.  **Add Sale**: Click the **"Add Sale"** button. If the data is valid, it will appear immediately in the history table below.
3.  **Error Handling**: If invalid data is entered (e.g., text in a numeric field), the system will alert you without crashing.
4.  **View Results**: The **"Accumulated Total"** at the bottom updates automatically with every new entry.