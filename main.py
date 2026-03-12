from tkinter import messagebox, Tk
# Importamos la función de registro y la lista compartida desde tu otro archivo
from registrar import Add_sale, Sales

# --- CONFIGURACIÓN DE TKINTER ---
# Creamos la instancia principal (root) de Tkinter
root = Tk()
# .withdraw() oculta la ventana gris vacía que aparece por defecto al usar Tkinter
# Esto permite que solo veamos los cuadros de diálogo (pop-ups)
root.withdraw()

def main():
    # Bienvenida inicial al usuario
    messagebox.showinfo("Welcome", "Starting Sales Control System")
    
    # --- CICLO DE CONTROL ---
    # Usamos una variable booleana como 'bandera' para controlar el bucle
    continuar = True
    while continuar:
        # Llamamos a la función que definiste en el otro archivo
        Add_sale()
        
        # askyesno devuelve True si el usuario pulsa "Sí" y False si pulsa "No"
        # Esto actualiza nuestra variable 'continuar' automáticamente
        continuar = messagebox.askyesno("Confirm", "Do you want to add another sale?")

    # --- GENERACIÓN DE REPORTE FINAL ---
    # Verificamos si la lista 'Sales' tiene elementos antes de procesar
    if Sales:
        report = "--- Sales History ---\n"  
        # Iteramos sobre la lista de diccionarios para construir una cadena de texto
        for s in Sales:
            report += f"Product: {s['product']} | Total: ${s['total']:.2f}\n"
        
        # Calculamos la suma de todos los campos 'total' usando una expresión generadora
        total_sum = sum(s['total'] for s in Sales)
        report += f"\nAccumulated total: ${total_sum:.2f}"
        
        # Mostramos el resumen acumulado en una ventana informativa
        messagebox.showinfo("Final Report", report)
    else:
        # Si el usuario cerró las ventanas sin registrar nada, lanzamos un aviso
        messagebox.showwarning("Notice", "No sales were recorded.")

    # Mensaje de despedida antes de que el script termine su ejecución
    messagebox.showinfo("Exit", "System closed. Have a great day!")

# Punto de entrada estándar de Python para ejecutar la función main
if __name__ == "__main__":
    main()