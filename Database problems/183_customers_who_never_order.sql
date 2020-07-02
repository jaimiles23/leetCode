/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-07-02 13:12:47
 * @modify date 2020-07-02 13:12:47
 * @desc [
    Solution to 183. [Customers who never order](https://leetcode.com/problems/customers-who-never-order/)

    - Requires subquery of Orders.CustomerId
    - Select all customers NOT in subquery
 ]
 */


SELECT Customers.Name AS 'Customers'
FROM Customers
WHERE Customers.id not in
(
    select CustomerId from Orders    
)

/*
Runtime: 951 ms, faster than 34.05% of MySQL online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
*/