/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-01 20:50:45
 * @modify date 2020-09-01 20:50:45
 * @desc [
     Solution to 1179. Reformat Department Table
    
    NOTES:
    - Create separate variables for each month
    - Group by ID per instruction
    - SUM(IF()) is a conditional summation in MYSQL
 ]
 */

SELECT 
    id,
    SUM( IF( month = 'Jan', revenue, NULL)) AS Jan_Revenue,
    SUM( IF( month = 'Feb', revenue, NULL)) AS Feb_Revenue,
    SUM( IF( month = 'Mar', revenue, NULL)) AS Mar_Revenue,
    SUM( IF( month = 'Apr', revenue, NULL)) AS Apr_Revenue,
    SUM( IF( month = 'May', revenue, NULL)) AS May_Revenue,
    SUM( IF( month = 'Jun', revenue, NULL)) AS Jun_Revenue,
    SUM( IF( month = 'Jul', revenue, NULL)) AS Jul_Revenue,
    SUM( IF( month = 'Aug', revenue, NULL)) AS Aug_Revenue,
    SUM( IF( month = 'Sep', revenue, NULL)) AS Sep_Revenue,
    SUM( IF( month = 'Oct', revenue, NULL)) AS Oct_Revenue,
    SUM( IF( month = 'Nov', revenue, NULL)) AS Nov_Revenue,
    SUM( IF( month = 'Dec', revenue, NULL)) AS Dec_Revenue

FROM 
    Department
GROUP BY
    id
