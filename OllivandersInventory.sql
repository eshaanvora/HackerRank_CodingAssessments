SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands as w
JOIN Wands_property as p
ON p.code = w.code
WHERE p.is_evil = 0
AND w.coins_needed =
(SELECT MIN(w1.coins_needed)
FROM Wands as w1
JOIN Wands_property as p1
ON p1.code = w1.code
WHERE w1.power = w.power AND p1.age = p.age)
ORDER BY w.power DESC, p.age DESC;

/*
SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands as w
JOIN Wands_property as p
ON p.code = w.code
WHERE p.is_evil = 0
AND w.coins_needed = 4654
ORDER BY w.coins_needed, w.power DESC, p.age DESC;
*/

/*
SELECT coins_needed, COUNT(coins_needed)
FROM Wands
GROUP BY coins_needed
ORDER BY COUNT(coins_needed) DESC;
*/

/* Group by function returns a list of each of the minimum coins needed per grouping of (power,age)
Instead we want pass our filter upward to another filter. If we pass the list up to our filter, we will select a coin value everytime there is a matching (power,age) grouping in the minimum coins list. Instead we only want to select a value per grouping of (power,age)

WHERE:
1 value per grouping of (power,age)
GROUP BY:
1 value per matching entry with minimum coins list

/*
