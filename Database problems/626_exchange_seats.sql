/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-08 14:07:15
 * @modify date 2020-09-08 14:07:15
 * @desc [
    Solution to 626. Exchange seats SQL
        https://leetcode.com/problems/exchange-seats/
 ]
 */

/* 
SQL statement to switch adjacent ID numbers

Process:
- Use MOD(id, 2). If odd +1, if even, -1
- if last student is odd, isn't renumbered.
*/

SELECT
    CASE
        WHEN 
            id = (SELECT MAX(id) FROM seat) AND
            (MOD(id, 2) = 1) 
                THEN id
        WHEN 
             MOD(id, 2) = 1 
                THEN id + 1
        ELSE 
            id - 1
    END AS id,
    student
FROM
    seat
ORDER BY
    id


