CREATE DATABASE IF NOT EXISTS realestate_db;
USE realestate_db;

-- Agents Table
CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    agency_name VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    customer_type ENUM('BUYER', 'SELLER') NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Properties Table
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT,
    title VARCHAR(150),
    description TEXT,
    type ENUM('APARTMENT', 'HOUSE', 'LAND', 'COMMERCIAL'),
    status ENUM('AVAILABLE', 'SOLD', 'RENTED', 'UNDER_CONTRACT') DEFAULT 'AVAILABLE',
    price DECIMAL(15,2),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    listed_date DATE,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Transactions Table
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    buyer_id INT,
    seller_id INT,
    sale_price DECIMAL(15,2),
    sale_date DATE,
    payment_method VARCHAR(50),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (buyer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (seller_id) REFERENCES customers(customer_id)
);

-- Visits Table
CREATE TABLE property_visits (
    visit_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    property_id INT,
    visit_date DATETIME,
    comments TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
