/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-06-30 17:24:19
 * @modify date 2020-06-30 17:24:19
 * @desc [
     Solution to 181 [Employees earning more than managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

     1. Cartesian join the two tables so all possible combinations are created
     2. Filter for correct matches b/w managerId & user ID, and Salary greater than Manager.
 ]
 */

SELECT 
    a.Name AS 'Employee'
FROM 
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
    AND a.Salary > b.Salary
;

/*
Runtime: 625 ms, faster than 43.58% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
*/

