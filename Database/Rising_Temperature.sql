-- LeetCode 197 - Rising Temperature
-- Problem: https://leetcode.com/problems/rising-temperature/
--
-- Approach: Self Join
--
-- How I Solved It:
-- 1. Join the Weather table with itself using two aliases:
--    w1 represents the current day and w2 represents the previous day.
-- 2. Use DATEDIFF to match rows where w1.recordDate is exactly
--    one day after w2.recordDate.
-- 3. Filter the joined rows so the current day's temperature
--    is greater than the previous day's temperature.
-- 4. Return the current day's id.
--
-- Key Learning:
-- A self join lets us compare rows from the same table.
-- DATEDIFF(recordDate1, recordDate2) = 1 identifies consecutive days.
--
-- Query performance depends on the database engine, indexes,
-- and query plan; there is no single fixed Big-O complexity for this SQL query.

SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
