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
* `cliente_dao.py`: Capa de acceso a datos con métodos estáticos para interactuar con la DB.
* `conexion.py`: Configuración del Pool de conexiones y métodos para obtener/liberar conexiones.
* `zona_fit_gui_App.py`: Lógica principal de la interfaz gráfica y eventos de usuario.

## 🔧 Configuración e Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/zona-fit-gym.git](https://github.com/TU_USUARIO/zona-fit-gym.git)
    ```

2.  **Configurar la Base de Datos:**
    * Crea una base de datos llamada `zona_fit_db`.
    * Crea la tabla `cliente` con las columnas: `id` (AI), `nombre`, `apellido` y `membresia`.
    * Ajusta las credenciales en `conexion.py` (Usuario: `root`, Password: `admin` por defecto).

3.  **Ejecutar la aplicación:**
    ```bash
    python zona_fit_gui_App.py
    ```

## 📸 Vista Previa
![Captura de pantalla de la App]([https://tu-enlace-a-la-imagen-aqui.png](https://github.com/Valduz-Jose/Aplicaciones-de-escritorio-con-Tkinter--GUI-Python-/blob/main/zona_fit_gui/screnshot.png?raw=true))

---
Desarrollado con ❤️ por Jose Alejandro Valduz Contreras
