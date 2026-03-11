from tkinter import messagebox, Tk
from registrar import Add_sale, Sales

# Ocultar la ventana raíz de Tkinter para que solo salgan los diálogos
root = Tk()
root.withdraw()

def main():
    messagebox.showinfo("Welcome", "Starting Sales Control System")
    
    # Ciclo principal adaptado a tu lógica de 'flag'
    continuar = True
    while continuar:
        Add_sale()
        
        # Usamos tu lógica de confirmación para seguir o salir
        continuar = messagebox.askyesno("Confirm", "Do you want to add another sale?")

    # Al finalizar, mostramos el resumen
    if Sales:
        report = "--- Sales History ---\n"  
        for s in Sales:
            report += f"Product: {s['product']} | Total: ${s['total']:.2f}\n"
        
        total_sum = sum(s['total'] for s in Sales)
        report += f"\nAccumulated total: ${total_sum:.2f}"
        
        messagebox.showinfo("Final Report", report)
    else:
        messagebox.showwarning("Notice", "No sales were recorded.")

    messagebox.showinfo("Exit", "System closed. Have a great day!")

if __name__ == "__main__":
    main()

