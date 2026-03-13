from tkinter import messagebox, simpledialog

# Global list to store dictionaries for each sale transaction
Sales = []

def Add_sale():
    # --- DATA INPUT ---
    # Use askstring to retrieve the product name (returns String or None if canceled)
    product_name = simpledialog.askstring("Product Data", "What is the product name?")
    
    # Check that the user didn't press "Cancel" or leave the name field empty
    if product_name: 
        try:
            # askfloat and askinteger automatically validate that the input is a numeric type
            unit_price = simpledialog.askfloat("Product Data", f"Price for {product_name}:")
            quantity_sold = simpledialog.askinteger("Product Data", f"Quantity of {product_name} sold:")
            
            # Ensure both values exist (checking that no window was canceled)
            if unit_price is not None and quantity_sold is not None:
                
                # --- PROCESSING ---
                # Calculate the total amount for the transaction
                total = quantity_sold * unit_price
                
                # Structure the information into a dictionary for easy access
                sale = {
                    "product": product_name,
                    "quantity": quantity_sold,
                    "unit price": unit_price,
                    "total": total
                }
                
                # Save the record into our main list
                Sales.append(sale)
                
                # --- OUTPUT / FEEDBACK ---
                # Display a success message with the total formatted to 2 decimal places
                messagebox.showinfo("Success", f"Product: {product_name}\nTotal: ${total:.2f}")
                
        except ValueError:
            # Handle any unexpected data conversion errors
            messagebox.showerror("Error", "Invalid data entered.")