import tkinter as tk
from registrar import SalesApp

def main():
    root = tk.Tk()
    # Instanciamos nuestra aplicación en la ventana raíz
    app = SalesApp(root)
    
    # El loop principal mantiene la ventana abierta
    root.mainloop()

if __name__ == "__main__":
    main()