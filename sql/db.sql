CREATE TYPE state_rol_type AS ENUM ('Active', 'Inactive');
CREATE TYPE document_type_enum AS ENUM ('TI', 'CC');
CREATE TYPE state_user_type_enum AS ENUM ('Active', 'Inactive');
CREATE TYPE state_provider_type AS ENUM ('Active', 'Inactive');

CREATE TABLE roles (
    id_rol SERIAL PRIMARY KEY,
    name_rol VARCHAR(100) NOT NULL UNIQUE,
    state state_rol_type NOT NULL DEFAULT 'Active',
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    type_document document_type_enum NOT NULL,
    document VARCHAR(100) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(100) NOT NULL,
    state state_user_type_enum NOT NULL DEFAULT 'Active',
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_access TIMESTAMPTZ,
    id_rol INTEGER NOT NULL REFERENCES roles(id_rol)
);

CREATE TABLE providers (
    id_provider SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    contact_name VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL,
    state state_provider_type NOT NULL DEFAULT 'Active',
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW()
);