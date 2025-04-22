-- View: Total Sales by City
CREATE VIEW city_sales_summary AS
SELECT city, COUNT(*) AS properties_sold, SUM(sale_price) AS total_revenue
FROM properties p
JOIN transactions t ON p.property_id = t.property_id
GROUP BY city;

-- View: Top Agents by Sales
CREATE VIEW top_agents AS
SELECT a.name, COUNT(*) AS deals_closed, SUM(t.sale_price) AS total_sales
FROM agents a
JOIN properties p ON a.agent_id = p.agent_id
JOIN transactions t ON p.property_id = t.property_id
GROUP BY a.name
ORDER BY total_sales DESC
LIMIT 5;
