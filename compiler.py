from database import Database
import re

def validate(query):

    select_reg = r"SELECT\s+?[^\s]+?\s+?FROM\s+?[^\s]"
    insert_reg = r"INSERT INTO\s+?[^\s]+?\s+?VALUES\(([0-9]*)"

    if re.search(select_reg,query):
            return 'SELECT'
    elif re.search(insert_reg,query):
        return 'INSERT'
    else:
        return 'INVALID'

def comp(dbname,query):

    db = Database(dbname, load=True)
    com = validate(query)

    try:
        if com=="SELECT":
            c = query.split("SELECT")
            s= c[1].split("FROM")
            col=s[0].strip()
            if col != '*':
                col = [col]
            table = s[1].strip()
            print(f"Command: {com}")
            print(f"Columns: {col}\nTable: {table}")
            answer = db.select(table,col)
            return answer
        elif com=="INSERT":
            s1=query.split("INTO")
            s2=s1[1].split("VALUES")
            s3=s2[1].split("(")
            s4=s3[1].split(")")

            table=s2[0].strip()
            val=s4[0].strip()
            val=val.split(',')
         
            print(f"Command: {com}")
            print(f"Table: {table}\nValues: {val}")
            db.insert(table,val)
            answer = (f"Inserted {val} into {table}")
            return answer
        elif com=="INVALID":
            return "Invalid Statement"
    except:
        return 'Error,Check SQL syntax'
        
    return 'Error,Check SQL syntax'
		
		
