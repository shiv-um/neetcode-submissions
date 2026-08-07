-- Write your query below
WITH acc_bal AS (
    SELECT account, SUM(amount) AS balance
    FROM transactions
    GROUP BY account
    HAVING SUM(amount) > 10000
)
SELECT name, balance
FROM users u
JOIN acc_bal a 
ON u.account = a.account;
