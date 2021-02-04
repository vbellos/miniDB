# miniDB with Server-Client support

Original Repository For Server-Client addon https://github.com/vbellos/Server-for-miniDB

The miniDB project is a minimal and easy to expand and develop for RMDBS tool, written excusivelly in Python 3. MiniDB's main goal is to provide the user with as much functionality as posssible while being easy to understand and even easier to expand. Thus, miniDB's primary market are students and researchers that want to work with a tool that they can understand through and through, while being able to implement additional features as quickly as possible.

## Installation

Python 3.7 or newer is needed. To download and build the project run:

```bash
git clone https://github.com/vbellos/miniDB.git
cd miniDB
pip install -r requirements.txt
```
## Documentation

The file [documentation.pdf](documentation.pdf) contains a detailed description of the miniDB library (in Greek).

##Server Queries:

SELECT COL1,COL2,COLn FROM TABLE

SELECT * FROM TABLE

INSERT INTO TABLE VALUES(VAL1,VAL2,VALn)

## Loading the [smallRelations database](https://www.db-book.com/db6/lab-dir/sample_tables-dir/index.html)

To create a database containing the smallRelations tables and get an interactive shell, run
``` Python
python -i smallRelationsInsertFile.py
```
You can the access the database through the db object that will be available. For example, you can show the contents of the student table by running the following command:
```python
>> db.show_table('student')
```
The database wil be save with the name `smdb`. You can load the database in a separate Python shell by running the following commands:
```python
>> from database import Database
>> db = Database("smdb", load=True)
```




## MiniDB Contributors
George S. Theodoropoulos, Yannis Kontoulis, Yannis Theodoridis; Data Science Lab., University of Piraeus.

##Addon Contributors
Vaggelis Bellos,Liana Tymplalexi,Lydia Bellonia
