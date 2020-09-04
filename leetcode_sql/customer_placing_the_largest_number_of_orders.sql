SELECT customer_number from ( 
    SELECT customer_number, val from (
        SELECT customer_number, COUNT(customer_number) as val from orders GROUP BY customer_number) AS T WHERE val in (
            SELECT MAX(val) as val from (SELECT COUNT(customer_number) as val from orders GROUP BY customer_number) AS T)) AS T;