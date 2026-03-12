from tkinter import messagebox, simpledialog

# Lista global para almacenar los diccionarios de cada venta
Sales = []

def Add_sale():
    # --- ENTRADA DE DATOS ---
    # Usamos askstring para obtener el nombre (devuelve String o None si se cancela)
    product_name = simpledialog.askstring("Product Data", "What is the product name?")
    
    # Verificamos que el usuario no haya presionado "Cancelar" o dejado vacío el nombre
    if product_name: 
        try:
            # askfloat y askinteger validan automáticamente que el tipo de dato sea numérico
            unit_price = simpledialog.askfloat("Product Data", f"Price for {product_name}:")
            quantity_sold = simpledialog.askinteger("Product Data", f"Quantity of {product_name} sold:")
            
            # Verificamos que ambos valores existan (que no se haya cancelado ninguna ventana)
            if unit_price is not None and quantity_sold is not None:
                
                # --- PROCESAMIENTO ---
                # Calculamos el monto total de la transacción
                total = quantity_sold * unit_price
                
                # Estructuramos la información en un diccionario para fácil acceso
                sale = {
                    "product": product_name,
                    "quantity": quantity_sold,
                    "unit price": unit_price,
                    "total": total
                }
                
                # Guardamos el registro en nuestra lista principal
                Sales.append(sale)
                
                # --- SALIDA / FEEDBACK ---
                # Mostramos un mensaje de éxito con el total formateado a 2 decimales
                messagebox.showinfo("Success", f"Product: {product_name}\nTotal: ${total:.2f}")
                
        except ValueError:
            # En caso de que ocurra un error inesperado en la conversión de datos
            messagebox.showerror("Error", "Invalid data entered.")