# 💼 Registro de Empleados (Python + Tkinter + MySQL)

Una aplicación de escritorio desarrollada en **Python**, con **interfaz gráfica (Tkinter)** y conexión a **MySQL**, que permite **registrar, visualizar y eliminar empleados** de forma sencilla.  
El proyecto está construido con **Programación Orientada a Objetos (POO)** y buenas prácticas de código.

---

## 🚀 Funcionalidades principales
✅ **Ver empleados:** muestra todos los registros almacenados en la base de datos.  
✅ **Agregar empleado:** permite ingresar nombre, sexo y correo (ID generado automáticamente).  
✅ **Eliminar empleado:** elimina un registro seleccionado de la tabla.  
✅ **Interfaz moderna y amigable:** desarrollada con `Tkinter` y `ttk.Treeview`.  
✅ **Conexión segura:** todas las consultas SQL están parametrizadas (sin riesgo de inyección).  
✅ **Creación automática de la tabla:** si la tabla `empleados` no existe, se crea al iniciar.

---

## 🧠 Tecnologías utilizadas
- **Python 3.8+**
- **Tkinter** (para la interfaz gráfica)
- **MySQL** (para la base de datos)
- **mysql-connector-python** (para conectar Python con MySQL)

---

## ⚙️ Instalación y configuración

# 1️⃣ Instala los requisitos
Abre una terminal y ejecuta:

```bash
pip install mysql-connector-python
💡 Tkinter ya viene incluido con Python en Windows y la mayoría de distribuciones de Linux.
Si no lo tienes, en Ubuntu puedes instalarlo con:

bash
Copiar código
sudo apt install python3-tk
2️⃣ Crea la base de datos MySQL
Conéctate a MySQL y ejecuta:



sql
Copiar código
CREATE DATABASE empresa;
USE empresa;
No es necesario crear la tabla manualmente — el programa la genera automáticamente.



3️⃣ Configura la conexión en el código
En el archivo principal (registro_empleados_gui.py), ajusta tus credenciales si es necesario:

python
Copiar código
self.conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TuContraseña",
    database="empresa"
)



4️⃣ Ejecuta la aplicación
Desde la terminal, corre el programa:

bash
Copiar código
python registro_empleados_gui.py
Se abrirá la ventana gráfica del sistema.
Podrás agregar, visualizar y eliminar empleados fácilmente. 🎯





🗃️ Estructura de la base de datos
sql
CREATE TABLE empleados (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  sexo VARCHAR(20) NOT NULL,
  correo VARCHAR(100) NOT NULL
);




✨ Mejoras frente al ejemplo original
Mejora	Descripción
🔹 POO aplicada	Separación en clases: conexión y lógica de negocio
🔹 Seguridad	Consultas SQL parametrizadas (sin inyección)
🔹 Autocreación de tabla	No requiere crear manualmente la estructura
🔹 Validación de datos	Verifica campos vacíos antes de insertar
🔹 Interfaz mejorada	Combobox, Treeview, botones y colores
🔹 Retroalimentación	Mensajes de error, éxito y advertencias



<img width="1536" height="1024" alt="TOPICOS TRA" src="https://github.com/user-attachments/assets/2f067c1d-037d-4925-8c73-7b18ee6f49fb" />
