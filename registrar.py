from tkinter import messagebox, simpledialog

Sales = []

def Add_sale():
    # Pedimos los datos mediante ventanas emergentes
    product_name = simpledialog.askstring("Product Data", "What is the product name?")
    
    if product_name: # Verificamos que no haya cancelado la ventana
        try:
            unit_price = simpledialog.askfloat("Product Data", f"Price for {product_name}:")
            quantity_sold = simpledialog.askinteger("Product Data", f"Quantity of {product_name} sold:")
            
            if unit_price is not None and quantity_sold is not None:
                total = quantity_sold * unit_price
                
                sale = {
                    "product": product_name,
                    "quantity": quantity_sold,
                    "unit price": unit_price,
                    "total": total
                }
                
                Sales.append(sale)
                
                # Confirmación visual del registro
                messagebox.showinfo("Success", f"Product: {product_name}\nTotal: ${total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid data entered.")