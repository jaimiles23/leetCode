/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 13:49:14
 * @modify date 2020-09-01 13:51:36
 * @desc [
    Solution to leetcode problem 627: Swap Salary https://leetcode.com/problems/swap-salary/

    This problem requires that the table be updated with a single statement. To complete this, use a CASE control structure to re-arrange
    the salary table's sex column.
 ]
 */


UPDATE
    salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;