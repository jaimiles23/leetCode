/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-06-29 21:40:36
 * @modify date 2020-06-29 21:40:36
 * @desc [
    Contains solution to 176 [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)
    
    Orders table by Salary in Ascending order and then returns 2nd highest salary.

    1. Select 1 distinct value from table
    2. Order table by salary in descending order
    3. Limit to a single value select and offset the value by 1 (to start at 2)
    4. IfNull argument accounts for if only 1 value in table
    5. outer select takes value from IfNull.
    ]
 */

SELECT
    IFNULL((
        SELECT DISTINCT Salary
        FROM Employee
        Order by Salary DESC
            LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;

/*
Runtime: 196 ms, faster than 95.78% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
*/