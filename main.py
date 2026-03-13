from tkinter import messagebox, Tk
# Import the registration function and the shared list from your other file
from registrar import Add_sale, Sales

# --- TKINTER CONFIGURATION ---
# Create the main Tkinter instance (root)
root = Tk()
# .withdraw() hides the empty gray window that appears by default in Tkinter
# This ensures only the dialog boxes (pop-ups) are visible
root.withdraw()


def main():
    # Initial welcome message for the user
    messagebox.showinfo("Welcome", "Starting Sales Control System")
    
    # --- CONTROL LOOP ---
    # Use a boolean variable as a 'flag' to control the loop
    continuar = True
    while continuar:
        # Call the function defined in the external registrar file
        Add_sale()
        
        # askyesno returns True if the user clicks "Yes" and False if "No"
        # This updates our 'continuar' variable automatically
        continuar = messagebox.askyesno("Confirm", "Do you want to add another sale?")

    # --- FINAL REPORT GENERATION ---
    # Check if the 'Sales' list contains any elements before processing
    if Sales:
        report = "--- Sales History ---\n"  
        # Iterate through the list of dictionaries to build a text string
        for s in Sales:
            report += f"Product: {s['product']} | Total: ${s['total']:.2f}\n"
        
        # Calculate the sum of all 'total' fields using a generator expression
        total_sum = sum(s['total'] for s in Sales)
        report += f"\nAccumulated total: ${total_sum:.2f}"
        
        # Display the accumulated summary in an information window
        messagebox.showinfo("Final Report", report)
    else:
        # If the user closed windows without registering anything, show a warning
        messagebox.showwarning("Notice", "No sales were recorded.")

    # Farewell message before the script ends execution
    messagebox.showinfo("Exit", "System closed. Have a great day!")

# Standard Python entry point to execute the main function
if __name__ == "__main__":
    main()

    