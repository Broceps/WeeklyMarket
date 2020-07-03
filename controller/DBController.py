import psycopg2

class DBController:
    _connection_str = open("../_files/db_connection_string.txt").read()

    def get_emails_and_ticker(self):
        conn = psycopg2.connect(self._connection_str)
        print ("Opened database successfully")
        cur = conn.cursor()
        cur.execute("SELECT u.email, s.ticker, u.first_name FROM users as u JOIN users_subscribed_company as s ON u.id = s.user_id;");
        rows = cur.fetchall()
        conn.commit()
        conn.close()

        return rows


