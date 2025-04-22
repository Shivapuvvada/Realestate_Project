-- Agents
INSERT INTO agents (name, email, phone, agency_name)
VALUES ('Alex Morgan', 'alex@primeprop.com', '1234567890', 'Prime Properties');

-- Customers
INSERT INTO customers (full_name, email, phone, customer_type)
VALUES ('John Doe', 'john@example.com', '9876543210', 'BUYER'),
       ('Emily Rose', 'emily@example.com', '7654321987', 'SELLER');

-- Properties
INSERT INTO properties (agent_id, title, type, price, city, state, country, listed_date)
VALUES (1, 'Modern 2BHK Apartment', 'APARTMENT', 250000.00, 'Austin', 'TX', 'USA', '2023-06-01');

-- Transactions
INSERT INTO transactions (property_id, buyer_id, seller_id, sale_price, sale_date, payment_method)
VALUES (1, 1, 2, 245000.00, '2023-07-15', 'Bank Transfer');

-- Visits
INSERT INTO property_visits (customer_id, property_id, visit_date, comments)
VALUES (1, 1, NOW(), 'Nice location. Considering offer.');
