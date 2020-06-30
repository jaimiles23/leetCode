/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-06-29 21:54:56
 * @modify date 2020-06-29 21:54:56
 * @desc [
    Solution to 182. [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

    1. Subquery to return all values, with counts
    2. Select from query where count >= 2
 ]
 */

select EMAIL from (    
    SELECT Email, COUNT(Email) AS EMAIL_COUNT
    FROM Person
    GROUP BY Email
    ) as E_COUNT
    WHERE EMAIL_COUNT >= 2
;

/*
Runtime: 615 ms, faster than 37.69% of MySQL online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
*/