-- Insertar usuario Admin
-- IMPORTANTE: Generar el hash con hash.py antes de insertar
INSERT INTO users (name, last_name, type_document, document, username, phone, email, password_hash, state, creation_date, last_access, id_rol)
VALUES (
    'Admin',
    'Obando',
    'CC',
    '123456789',
    'admin',
    '3000000000',
    'admin@obansoft.com',
    '$2b$12$yF082trrH764MBb/MK0FbO6CehQ0Iwx6nFqIA5YoVW5g6CDmO7rWe',
    'Active',
    NOW(),
    NULL,
    1
);