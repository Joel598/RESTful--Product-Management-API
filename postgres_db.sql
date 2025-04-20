
-- Create product table
CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    price FLOAT NOT NULL
);
