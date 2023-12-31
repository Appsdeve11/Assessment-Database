### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
its a database management system 

- What is the difference between SQL and PostgreSQL?
when you PostgreSQL you can use SQL along with its own language PL/pgSQL which can create functions and add structure to SQL. 


- In `psql`, how do you connect to a database?
you would need to know...
-the name of your target database
-the host name
-port number of the server 
-and the username you want to connect as

- What is the difference between `HAVING` and `WHERE`?
The WHERE clause evaluates all rows, the HAVING clause evaluates rows but only after they have been put formed into the data.

- What is the difference between an `INNER` and `OUTER` join?
the difference between inner join and outer join is that the inner keeps information from the table that relate to one another, while outer join can keep information that is not related to each other.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A left outer join has all records of the "left" table even if the "right" table does not match what is specified. A right outer join is pretty much the opposite, it contains information from the "right" table even if there no matches in the "left" table. 

- What is an ORM? What do they do?
ORM stands for Object Relational Mapper. it's a software that translates data representations.
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  -AJAX requests are executed in the browser, while server-side requests using requests are executed on the server.
  -AJAX requests made from the browser may require additional steps for authentication, such as sending cookies or tokens. 

- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for Cross-Site Request Forgery. It is a type of security vulnerability that allows an attacker to trick a user into unintentionally performing actions on a website without their consent or knowledge.


- What is the purpose of `form.hidden_tag()`?
the purpose for form.hidden_tag is to protect you from CSRF attacks.
