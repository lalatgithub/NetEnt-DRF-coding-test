##### Tested Enviroment
```
Python 2.7
Python 3.4
Django 1.10
Django Rest Framework 3.5
SQLite
Ubuntu 14.04
```

##### Switch to project root directory and run below command to install project dependencies
```
pip install -r requirements.txt
```

##### API Endpoints
```
<http://localhost:8000/api-auth/login/>

<http://localhost:8000/api-auth/logout/>

<http://localhost:8000/add_book/>

<http://localhost:8000/update_book/{pk}/>

<http://localhost:8000/add_genre/>
```

##### Available Users for testing purposes
```
user: demo1
pass: demo1

user: demo2
pass: demo2
```

##### Validations
```
1. The author should automatically be selected based on the logged in user.

2. Only the author should be able to update his/her book.

3. A book title has to be unique per author (each author can have a book with the same title,
but an author can not have two books with the same title). 

4. An author is only allowed to have 5 books at one time.
```
