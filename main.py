import mysql.connector as connector

def connection():

    config = {
        "user": "<user>",
        "password": "<password>",
        "host": "remotemysql.com",
        "port": 3306,
        "database": "UdI8EZnZLb"
    }
    try:
        c = connector.connect(**config)
        return c
    except:
        print ("connection error")
        exit(1)

def query_exec(query):
    cn = connection()
    cur = cn.cursor()
    cur.execute(query)
    r = cur.fetchall()
    return r

atomic_no = input("Enter Atomic Number Of Element to Fetch Data: ")
q = "select name,atomic_number,atomic_weight,electron_configuration from elements where atomic_number = "+ atomic_no
data = query_exec(q)[0]

print('Name','\t','Atomic Number','\t','Atomic Weight','\t','Electronic Configuration')
print(data[0],'\t',data[1],'\t','\t',data[2],'\t',data[3])
