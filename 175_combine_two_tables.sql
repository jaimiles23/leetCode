/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-06-29 21:34:34
 * @modify date 2020-06-29 21:34:34
 * @desc [
    Solution to problem 175. [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)
 ]
 */

Select 
   Person.FirstName, Person.LastName, 
   Address.City, Address.State 
   FROM Person 
      LEFT JOIN Address
      ON Person.PersonId = Address.PersonId


/*
Runtime: 403 ms, faster than 71.71% of MySQL online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
*/