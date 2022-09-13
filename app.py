from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    number = init_db()

    return 'This is the ' + str(number[0]) + ' time you have visited this page !'


def init_db():
    conn = psycopg2.connect(
        host="ec2-54-228-125-183.eu-west-1.compute.amazonaws.com",
        port="5432",
        database="desehotlma73gv",
        user="pgkzzmxwroynhr",
        password="26c5bebc39ecd86874e24b90526f07aa3abe74900aaa8178a582284309333a29"
    )
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('CREATE TABLE IF NOT EXISTS counter (count integer)')

    # Insert data into the table
    cur.execute('INSERT INTO counter (count) SELECT (0) WHERE NOT EXISTS (SELECT * FROM counter)')

    # Increment counter
    cur.execute('UPDATE counter SET count = count + 1')

    # Make the changes to the database persistent
    conn.commit()

    cur.execute('SELECT count FROM counter')
    rows = cur.fetchone()

    # Close communication with the database
    cur.close()
    conn.close()

    return rows


if __name__ == '__main__':
    app.run(debug=True)
