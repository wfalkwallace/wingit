SQL Table Structure

===================

table | feature | feature | feature | feature | feature | feature | feature | feature | feature | feature
:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-
flights | flight_id | origin (airport/id) | dest (airport/id) | etd | eta | ~~duration~~ | ~~connections?~~ | ~~nearest city~~ | ~~open seats~~ | price
features | feature_id | place (airport/id) | temp | beer_price
airports | airport_id | code | name | city | country 


---

SQL DB Setup
============
(For RDS dev instance)


- At the command prompt, type:

`mysql -h ??? -u root -p wingitdb`
and enter password `wingitrealgood`.

- At the MySQL prompt you should now see, copy paste (the whole things):

```
DROP TABLE airports;
DROP TABLE flights;
DROP TABLE features;
```
Then

```
CREATE TABLE airports(
	airport_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	code VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
	city VARCHAR(64) NULL,
	country VARCHAR(64) NOT NULL,
	created_at DATETIME
);

CREATE TABLE flights(
	flight_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	origin INT NOT NULL,
	dest INT NOT NULL,
	etd DATETIME NOT NULL,
	eta DATETIME NOT NULL,
	price DECIMAL NOT NULL,
	created_at DATETIME,

	FOREIGN KEY (origin, dest) 
	        REFERENCES airports(airport_id)
	        ON DELETE CASCADE
);

CREATE TABLE features(
	feature_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	place INT NOT NULL,
	temp INT NOT NULL,
	beer_price DECIMAL NOT NULL,
	created_at DATETIME,

	FOREIGN KEY (place) 
	        REFERENCES airports(airport_id)
	        ON DELETE CASCADE
);

```