import tkinter as tk
from tkinter import ttk  # Usamos ttk para widgets más modernos (como el Treeview)
from tkinter import messagebox
import sqlite3
import os

class EmployeeApp(tk.Frame):
    """
    Aplicación de registro de empleados con GUI (Tkinter) y BD (SQLite).
    Cumple con los requisitos de POO  y modularidad[cite: 22].
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sistema de Registro de Empleados")
        self.master.geometry("650x500")
        
        # Define la base de datos
        self.db_name = 'empleados.db'
        self.init_db()
        
        # Construye la GUI
        self.create_widgets()
        
        # Carga los empleados existentes al iniciar
        self.view_employees()

    def init_db(self):
        """Inicializa la base de datos y la tabla si no existen."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # El ID se genera automáticamente 
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            ''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo inicializar la DB: {e}")
            self.master.quit()

    def run_query(self, query, parameters=()):
        """Ejecuta consultas de forma segura """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
                return result
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Error en la consulta: {e}")
            return None

    def create_widgets(self):
        """Crea todos los elementos de la interfaz gráfica [cite: 12]"""
        
        # --- Frame para los campos de entrada ---
        input_frame = tk.LabelFrame(self.master, text="Datos del Empleado")
        input_frame.pack(fill="x", expand="no", padx=10, pady=10)

        tk.Label(input_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(input_frame, width=40)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Sexo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.sex_entry = tk.Entry(input_frame, width=40)
        self.sex_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Correo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = tk.Entry(input_frame, width=40)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # --- Frame para los botones de acción ---
        button_frame = tk.Frame(self.master)
        button_frame.pack(fill="x", expand="no", padx=10, pady=5)

        tk.Button(button_frame, text="Añadir Empleado", command=self.add_employee).pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(button_frame, text="Modificar Empleado", command=self.update_employee).pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(button_frame, text="Eliminar Empleado", command=self.delete_employee).pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(button_frame, text="Limpiar Campos", command=self.clear_fields).pack(side="left", fill="x", expand=True, padx=5)

        # --- Frame para la vista de empleados (Treeview) ---
        tree_frame = tk.Frame(self.master)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Sexo", "Correo"), show="headings", yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)

        # Definir encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("Correo", text="Correo")

        # Ajustar ancho de columnas
        self.tree.column("ID", width=50, stretch=tk.NO, anchor="center")
        self.tree.column("Nombre", width=200)
        self.tree.column("Sexo", width=100, anchor="center")
        self.tree.column("Correo", width=250)
        
        # Evento para seleccionar un item y llenar los campos
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)

    def view_employees(self):
        """Cumple con 'Ver empleados' [cite: 13]"""
        # Limpiar vista previa
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # Consultar y poblar
        query = "SELECT * FROM employees"
        employees = self.run_query(query)
        if employees:
            for emp in employees:
                self.tree.insert("", "end", values=emp)

    def add_employee(self):
        """Cumple con 'Añadir empleado' [cite: 14, 15, 16, 17]"""
        name = self.name_entry.get()
        sex = self.sex_entry.get()
        email = self.email_entry.get()

        if not name or not sex or not email:
            messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios.")
            return
            
        query = "INSERT INTO employees (name, sex, email) VALUES (?, ?, ?)"
        parameters = (name, sex, email)
        
        if self.run_query(query, parameters):
            messagebox.showinfo("Éxito", "Empleado añadido correctamente.")
            self.clear_fields()
            self.view_employees()

    def update_employee(self):
        """Función para 'Modificar' (solicitada por el usuario)"""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona un empleado de la lista para modificar.")
            return

        # Obtener datos de los campos de entrada
        new_name = self.name_entry.get()
        new_sex = self.sex_entry.get()
        new_email = self.email_entry.get()
        
        if not new_name or not new_sex or not new_email:
            messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios.")
            return
            
        # Obtener el ID del empleado seleccionado
        emp_id = self.tree.item(selected_item)['values'][0]
        
        query = "UPDATE employees SET name = ?, sex = ?, email = ? WHERE id = ?"
        parameters = (new_name, new_sex, new_email, emp_id)
        
        if self.run_query(query, parameters):
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
            self.clear_fields()
            self.view_employees()

    def delete_employee(self):
        """Cumple con 'Eliminar empleado' [cite: 19]"""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona un empleado de la lista para eliminar.")
            return

        if not messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar a este empleado?"):
            return

        emp_id = self.tree.item(selected_item)['values'][0]
        
        query = "DELETE FROM employees WHERE id = ?"
        parameters = (emp_id,)
        
        if self.run_query(query, parameters):
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            self.clear_fields()
            self.view_employees()

    def on_item_select(self, event):
        """Al hacer clic en un empleado, rellena los campos de entrada."""
        selected_item = self.tree.focus()
        if not selected_item:
            return
            
        values = self.tree.item(selected_item)['values']
        self.clear_fields()
        
        self.name_entry.insert(0, values[1])  # Nombre
        self.sex_entry.insert(0, values[2])   # Sexo
        self.email_entry.insert(0, values[3]) # Correo

    def clear_fields(self):
        """Limpia los campos de entrada."""
        self.name_entry.delete(0, "end")
        self.sex_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        # Quita la selección del Treeview
        if self.tree.focus():
            self.tree.selection_remove(self.tree.focus())


# --- Bloque principal para ejecutar la aplicación ---
if __name__ == '__main__':
    root = tk.Tk()
    app = EmployeeApp(master=root)
    app.mainloop()
