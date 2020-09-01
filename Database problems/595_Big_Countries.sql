/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 13:35:57
 * @modify date 2020-09-01 13:35:57
 * @desc [
     Solution to 595. Big countries: https://leetcode.com/problems/big-countries/

     NOTE: Two available approaches. Can use either OR or Union between two different searches with WHERE clause. This has marginal performance increases.
 ]
 */

SELECT
    name, population, area
FROM 
    World
WHERE 
    (area > 3000000) OR 
    (population > 25000000)
;
