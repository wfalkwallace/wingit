SQL Table Structure
===================

flights:
id | from (airport/id) | to (airport/id) | etd | eta | *duration* | *connections?* | *nearest city* | *open seats* | price

features:
id | place (airport/id) | temp | beer_price

airports:
id | code | name | city | country 

---

SQL DB Setup
============
(For RDS dev instance)


- At the command prompt, type:

`mysql -h ??? -u root -p wingit_dev`
and enter password `wingit`.

- At the MySQL prompt you should now see, copy paste (the whole things):

```
DROP TABLE airports;
DROP TABLE flights;
DROP TABLE features;
```
Then

```
CREATE TABLE airports(
	id INT(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	code VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
	city VARCHAR(64) NOT NULL,
	country VARCHAR(64) NOT NULL,
	created_at DATETIME
);

CREATE TABLE flights(
	id INT(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	code VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
	city VARCHAR(64) NOT NULL,
	country VARCHAR(64) NOT NULL,
	created_at DATETIME
);

CREATE TABLE features(
	id INT(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	code VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
	city VARCHAR(64) NOT NULL,
	country VARCHAR(64) NOT NULL,
	created_at DATETIME
);

```