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
    'REEMPLAZAR_CON_HASH_GENERADO',
    'Active',
    NOW(),
    NULL,
    1
);