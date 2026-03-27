-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

-- 2. Crear la tabla cliente con la estructura que requiere tu código
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    membresia INT NOT NULL
);

-- 3. Insertar datos de prueba (opcional)
INSERT INTO cliente (nombre, apellido, membresia) VALUES ('Juan Carlos', 'Perez', 500);
INSERT INTO cliente (nombre, apellido, membresia) VALUES ('Alexa', 'Perez', 600);