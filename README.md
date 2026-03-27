# 🏋️‍♂️ Zona Fit - Sistema de Gestión de Gimnasio

**Zona Fit** es una aplicación de escritorio desarrollada en **Python** que permite la administración integral de clientes de un gimnasio. El sistema facilita las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) interactuando con una base de datos **MySQL** de forma eficiente.

## 🚀 Características Principales

* **Interfaz Gráfica (GUI):** Desarrollada con la librería `tkinter` y `ttk`, ofreciendo una experiencia de usuario intuitiva y organizada.
* **Arquitectura DAO (Data Access Object):** Separación clara entre la lógica de negocio y la persistencia de datos para un código mantenible y escalable.
* **Gestión de Base de Datos:** Implementación de un **Pool de Conexiones** mediante `mysql-connector-python` para optimizar el rendimiento y manejo de recursos.
* **Validación de Datos:** El sistema asegura que los campos obligatorios estén completos y que la membresía sea un valor numérico antes de procesar la información.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Base de Datos:** MySQL
* **Librería GUI:** Tkinter / TTK
* **Conector DB:** `mysql-connector-python` (utilizando `pooling`)

## 📋 Estructura del Proyecto

* `cliente.py`: Clase de modelo que representa la entidad Cliente.
* `cliente_dao.py`: Capa de acceso a datos con métodos para seleccionar, insertar, actualizar y eliminar registros.
* `conexion.py`: Configuración del Pool de conexiones para la base de datos `zona_fit_db`.
* `zona_fit_gui_App.py`: Lógica principal de la interfaz gráfica y gestión de eventos.

## 🔧 Configuración e Instalación (Plug & Play)

### 1. Clonar el repositorio
```bash
git clone https://github.com/Valduz-Jose/Aplicaciones-de-escritorio-con-Tkinter--GUI-Python-.git
cd Aplicaciones-de-escritorio-con-Tkinter--GUI-Python-
```

### 2. Configurar la Base de Datos
Ejecuta el siguiente script en tu gestor MySQL (como MySQL Workbench):

```bash
CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    membresia INT NOT NULL
);
```
### 3. Instalar dependencias
```bash
pip install mysql-connector-python
```
### 4. Ejecutar la aplicación
```bash
python zona_fit_gui_App.py
```

📸 Vista Previa
Desarrollado con fines educativos y profesionales por Jose Alejandro Valduz Contreras.
<img width="875" height="625" alt="Captura de pantalla 2026-03-27 135125" src="https://github.com/user-attachments/assets/4eda12cc-e648-409d-82fe-21032edb175e" />
