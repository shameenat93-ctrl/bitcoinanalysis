from flask import Flask, render_template
import psycopg2
Database_url=os.getenv("DATABASE_URL")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reports")
def reports():
    conn = psycopg2.connect(Database_url)
    cur = conn.cursor()

    cur.execute("""
        SELECT emp_id,
               emp_name,
               department,
               salary
        FROM employees
        ORDER BY emp_id
    """)

    employees = cur.fetchall()
    

    cur.close()
    conn.close()
    return render_template("reports.html")

if __name__ == "__main__":
    app.run()