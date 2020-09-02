/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 20:19:27
 * @modify date 2020-09-01 20:19:27
 * @desc [
     Solutions to 196. Delete Duplicate Emails
     https://leetcode.com/problems/delete-duplicate-emails/

     Solution 1: Join table on itself and delete larger ID numbers

     Solution 2: use GROUP BY and HAVING
 ]
 */

 /* Solution 1
1. GROUP BY
2. HAVING to identify duplicates
3. Delete all but 1 of the HAVING group
*/

DELETE
    p1
FROM 
    Person AS p1,
    Person AS p2
WHERE
    p1.Email = p2.Email AND
    p1.Id > p2.Id
    

/* Solution 2
Steps:
1. GROUP BY
2. HAVING to identify duplicates
3. Delete all but 1 of the HAVING group

Notes:
- MySQL doesn't support DELETE and SELECT from the same table.
    Thus, must use SELECT from temp table.
*/

DELETE 
FROM 
    Person 
WHERE Id NOT IN 
    (
        SELECT * 
        FROM
        (
            SELECT 
                MIN(Id) 
            FROM 
                Person 
        GROUP BY 
                Email
        ) as temp_table
    );

    

