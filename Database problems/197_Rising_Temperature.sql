/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 19:38:13
 * @modify date 2020-09-01 19:38:13
 * @desc [
    Solution to 197. Rising Temperature
    https://leetcode.com/problems/rising-temperature/

    NOTES:
    - MySQL uses the DateDiff formula to compare dates.
        - Need to use Table aliases to (INNER) JOIN table on itself
        - Create criteria on the JOIN so that the resulting table is the result.
 ]
 */

SELECT
    w1.id AS 'Id'
FROM
    weather as w1
JOIN
    weather as w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
    AND w1.Temperature > w2.Temperature        

