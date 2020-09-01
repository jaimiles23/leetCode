/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 13:35:57
 * @modify date 2020-09-01 13:41:43
 * @desc [
     Solution to 595. Big countries: https://leetcode.com/problems/big-countries/

     NOTE: Two available approaches. Can use either OR or Union between two different searches with WHERE clause. 

     Union is about ~ 25% faster. This is only true for this given table structure because there is not an index specifying both population and area.
     However, Union also performs DISTINCT operation which may be expensive in other data tables. 

     Ultimately, there is not enough information provided to know the better operation. Instead, requires explicit testing to optimize data retrieval.
 ]
 */


/*
OR Implementation
*/ 

SELECT
    name, population, area
FROM 
    World
WHERE 
    (area > 3000000) OR 
    (population > 25000000)
;


/* 
UNION Implementation
*/

SELECT 
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT 
    name, population, area
FROM
    world
WHERE
    population > 25000000
;