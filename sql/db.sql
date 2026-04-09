CREATE TYPE state_rol_type AS ENUM ('Active', 'Inactive');
CREATE TYPE document_type_enum AS ENUM ('TI', 'CC');
CREATE TYPE state_user_type_enum AS ENUM ('Active', 'Inactive');
CREATE TYPE state_provider_type_enum AS ENUM ('Active', 'Inactive');
CREATE TYPE state_category_type_enum AS ENUM ('Active', 'Inactive');
CREATE TYPE state_product_type_enum AS ENUM ('Active', 'Inactive'); ---En proceso de revision
CREATE TYPE payment_method_enum AS ENUM ('Efectivo', 'Nequi', 'Daviplata');
CREATE TYPE inventory_movement_enum AS ENUM ('IN', 'OUT');
CREATE TYPE cash_state_enum AS ENUM ('Open', 'Closed');

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
    state state_provider_type_enum NOT NULL DEFAULT 'Active',
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE categories (
    id_category SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(255),
    state state_category_type_enum NOT NULL DEFAULT 'Active',
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE products (
    id_product SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price NUMERIC(10,2) NOT NULL,
    size VARCHAR(50),
    color VARCHAR(50),
    stock INTEGER NOT NULL DEFAULT 0,
    state state_product_type_enum NOT NULL DEFAULT 'Active', ---Proceso de revision
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    id_category INTEGER NOT NULL REFERENCES categories(id_category),
    id_provider INTEGER NOT NULL REFERENCES providers(id_provider)
);

CREATE TABLE inventory_movements (
    id_movement SERIAL PRIMARY KEY,
    movement_type inventory_movement_enum NOT NULL,
    quantity INTEGER NOT NULL,
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    id_product INTEGER NOT NULL REFERENCES products(id_product),
    id_user INTEGER NOT NULL REFERENCES users(id_user)
);

CREATE TABLE sales (
    id_sale SERIAL PRIMARY KEY,
    total NUMERIC(10,2) NOT NULL,
    payment_method payment_method_enum NOT NULL,
    creation_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    id_user INTEGER NOT NULL REFERENCES users(id_user)
);

CREATE TABLE sale_details (
    id_detail SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    subtotal NUMERIC(10,2) NOT NULL,
    id_sale INTEGER NOT NULL REFERENCES sales(id_sale),
    id_product INTEGER NOT NULL REFERENCES products(id_product)
);

CREATE TABLE cash_register (
    id_cash SERIAL PRIMARY KEY,
    initial_amount NUMERIC(10,2) NOT NULL,
    total_sales NUMERIC(10,2),
    state cash_state_enum NOT NULL DEFAULT 'Open',
    opened_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    closed_at TIMESTAMPTZ,
    id_user INTEGER NOT NULL REFERENCES users(id_user)
);