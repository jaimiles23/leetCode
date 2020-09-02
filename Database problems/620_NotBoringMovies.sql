/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 19:24:42
 * @modify date 2020-09-01 19:24:42
 * @desc [
    Solution to problem #620: Not Boring Movies
    https://leetcode.com/problems/not-boring-movies/

    Notes:
        - Modulus operator used in SQL
        - indenting between different key words
 ]
 */

SELECT
    id, movie, description, rating
FROM 
    cinema
WHERE
    id % 2 = 1 AND
    description != 'boring'
ORDER BY
    rating DESC