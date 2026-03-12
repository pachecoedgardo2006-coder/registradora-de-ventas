import tkinter as tk
from tkinter import messagebox, ttk

class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Control System")
        self.root.geometry("500x550")
        
        self.sales_list = []

        # --- Interfaz de Entrada ---
        frame_entry = tk.LabelFrame(self.root, text=" Register New Sale ", padx=10, pady=10)
        frame_entry.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_entry, text="Product Name:").grid(row=0, column=0, sticky="w")
        self.ent_name = tk.Entry(frame_entry)
        self.ent_name.grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(frame_entry, text="Unit Price ($):").grid(row=1, column=0, sticky="w")
        self.ent_price = tk.Entry(frame_entry)
        self.ent_price.grid(row=1, column=1, pady=5, sticky="ew")

        tk.Label(frame_entry, text="Quantity:").grid(row=2, column=0, sticky="w")
        self.ent_qty = tk.Entry(frame_entry)
        self.ent_qty.grid(row=2, column=1, pady=5, sticky="ew")

        btn_add = tk.Button(frame_entry, text="Add Sale", command=self.validate_and_add, bg="#E70FA6", fg="white")
        btn_add.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # --- Tabla de Historial (Treeview) ---
        frame_list = tk.LabelFrame(self.root, text=" Sales History ", padx=10, pady=10)
        frame_list.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_list, columns=("Qty", "Total"), height=8)
        self.tree.heading("#0", text="Product")
        self.tree.heading("Qty", text="Qty")
        self.tree.heading("Total", text="Total ($)")
        self.tree.column("#0", width=150)
        self.tree.column("Qty", width=50)
        self.tree.column("Total", width=80)
        self.tree.pack(fill="both", expand=True)

        # --- Resumen Final ---
        self.lbl_total = tk.Label(self.root, text="Accumulated Total: $0.00", font=("Arial", 12, "bold"))
        self.lbl_total.pack(pady=10)

    def validate_and_add(self):
        """Verifica que los datos sean correctos antes de registrar."""
        name = self.ent_name.get().strip()
        
        try:
            # Validaciones automáticas de tipo de dato
            price = float(self.ent_price.get())
            qty = int(self.ent_qty.get())
            
            if not name:
                raise ValueError("Name is empty")
            if price <= 0 or qty <= 0:
                raise ValueError("Values must be positive")

            total_sale = price * qty
            self.sales_list.append({"product": name, "total": total_sale})
            
            # Actualizar Interfaz
            self.tree.insert("", "end", text=name, values=(qty, f"{total_sale:.2f}"))
            self.update_summary()
            
            # Limpiar campos
            self.ent_name.delete(0, tk.END)
            self.ent_price.delete(0, tk.END)
            self.ent_qty.delete(0, tk.END)
            self.ent_name.focus()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid Name, Price (number), and Quantity (integer).")

    def update_summary(self):
        total_sum = sum(s['total'] for s in self.sales_list)
        self.lbl_total.config(text=f"Accumulated Total: ${total_sum:.2f}")