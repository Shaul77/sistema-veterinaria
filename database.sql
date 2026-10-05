-- Creacion de la base de datos para la veterinaria
CREATE DATABASE IF NOT EXISTS veterinaria_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Creacion del usuario de aplicacion
CREATE USER IF NOT EXISTS 'sistema_veterinaria'@'%' IDENTIFIED BY 'veterinaria12345';

-- Concesion de todos los privilegios sobre la base de datos
GRANT ALL PRIVILEGES ON veterinaria_db.* TO 'sistema_veterinaria'@'%';

-- Aplicacion inmediata de los permisos
FLUSH PRIVILEGES;