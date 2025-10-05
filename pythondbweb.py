import psycopg2
from fastapi import FastAPI

app = FastAPI()
#  uvicorn pythondbweb:app --reload used for api as postman to give value or retrieve it.

def dbconn() :
    return psycopg2.connect(
    dbname = "mydb",
    user = "root",
    password = "Ayush@123",
    host = "localhost",
    port = "5432"
)

@app.post("/users")
def send(name : str, email : str) :
    conn = dbconn()
    cur = conn.cursor()

    cur.execute("insert into users (name, email) values (%s,%s)",(name,email))
    conn.commit()

    cur.close()
    conn.close()

    return {f"user Successfully Added name : {name} email : {email}"}

@app.get("/users")
def dispaly() : 
    conn = dbconn()
    cur = conn.cursor()

    cur.execute("select * from users")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {f"users : {rows}"}