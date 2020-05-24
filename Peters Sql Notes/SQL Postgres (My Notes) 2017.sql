-- THE 'LIKE' and 'ILIKE' STATEMENT (case sensitive, use ILIKE instead for case insensitivity) (With Wildcard), can also use "NOT LIKE".  Underscore stands for a single character.  % is any sequence of characters.
SELECT first_name, last_name FROM customer WHERE first_name LIKE 'Jen%'; -- starting with
SELECT first_name, last_name FROM customer WHERE first_name LIKE '%er'; -- ending with
SELECT first_name, last_name FROM customer WHERE first_name LIKE '%er%'; -- in the middle
SELECT first_name, last_name FROM customer WHERE first_name NOT LIKE 'Jen%';  -- not like
SELECT first_name, last_name FROM customer WHERE first_name LIKE '_her%'; -- single character missing and any number of chars can come after string
SELECT first_name, last_name FROM customer WHERE first_name ILIKE 'Jen%'; -- starting with...but case insensitive

-- NEED TO UNDERSTAND "IN STATEMENT" AND "SUB QUERIES"
SELECT customer_id, rental_id, return_date FROM rental WHERE customer_ID IN(1,2) ORDER BY return_date DESC; */ -- Example of "In"
SELECT customer_id, rental_id, return_date FROM rental WHERE customer_ID NOT IN(1,2,5) ORDER BY return_date DESC; */ -- EXAMPLE of "Not In"

-- Great example of finding a payment amount between two dates but notice that we're using strings, not integers!
SELECT amount, payment_date FROM payment WHERE payment_date BETWEEN '2007-02-07' AND '2007-02-15';

-- We can also use "NOT BETWEEN", but note, it does not include the numbers specified themselves, i.e. it isn't >=, it's just >
SELECT customer_id, amount FROM payment WHERE amount NOT BETWEEN 2.99 AND 3.99;

-- Examples of a BETWEEN statement, just a nice way of writing ">= 1 AND  <= 5"
SELECT customer_id, amount FROM payment WHERE amount BETWEEN 2.99 AND 3.99;
SELECT title, film_id
FROM film
WHERE film_id BETWEEN 1 AND 5
ORDER BY film_id ASC;

-- These examples both offer the same solution, but differ in how they get the answer:
SELECT title, film_id
FROM film
WHERE film_id >= 1 AND film_id <= 5
ORDER BY film_id ASC;
SELECT title, film_id
FROM film
ORDER BY film_id
LIMIT 5

/* IMPORTANT NOTE ABOUT ORDER BY, Postgres does allow you to order by columns not in the select clause, however, oracle, mysql etc don't. You need to select those columns that you want to order by, so always do that for easy db system translation */
SELECT first_name, last_name FROM customer ORDER BY first_name ASC, last_name DESC; /* This is like multiple level custom sort in Excel.  if first name was the same, the last name willl be ordered by last name descending - Multiple ORDER BY EXAMPLE */
SELECT first_name, last_name FROM customer ORDER BY first_name ASC; /* Great Example of Order By */
SELECT * FROM customer ORDER BY customer_id ASC; /* Orders Results by either ASC (the default) or DESC (you can also order by muliple columns by using a comma) */
SELECT * FROM customer LIMIT 20; /* This limits the result to 20 rows of results, useful to get all fields but only a few rows */
SELECT COUNT(*) FROM actor; /* This inquires as to how many rows are present (in the total table) based on the condition */
SELECT COUNT(actor_id) FROM actor; /* NOTE This doesn't consider Null Values in that column, This inquires as to how many rows are present (in only the column specified) based on the condition */
SELECT COUNT(DISTINCT actor_id) FROM actor; /* You can also write this as CCOUNT(DISTINCT(actor_id)) */
