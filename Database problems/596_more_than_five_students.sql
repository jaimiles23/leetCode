/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 19:57:29
 * @modify date 2020-09-01 19:58:10
 * @desc [
     Solution to # 596. More than 5 students.

Steps:
    - COUNT(*)
    - GROUP BY class
    - HAVING more than X students

NOTE:
    - use DISTINCT for duplicate students2

 ]
 */


SELECT
    class
FROM 
    courses
GROUP BY
    class
HAVING
    COUNT( DISTINCT(student)) >= 5