from db_connection import Connection

db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "project_test"


def get_user_mail_psw(email: str, password: str):
    try:
        conn = Connection(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        sql = f"SELECT email, password FROM user WHERE email = '{email}' AND password = '{password}'"
        cursor = conn.execute_query(sql=sql)
        data = cursor.fetchone()
        conn.disconnect()
        if data == None:
            return False
        else:
            return data
    except Exception as err:
        conn.rollback()
        print("There has been an error...\n", err)


def get_user_mail_only(email: str):
    try:
        conn = Connection(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        sql = f"SELECT email, id FROM user WHERE email = '{email}'"
        cursor = conn.execute_query(sql=sql)
        data = cursor.fetchone()
        conn.disconnect()
        if data == None:
            return False
        else:
            return data
    except Exception as err:
        conn.rollback()
        print("There has been an error...\n", err)


def update_password(new_psw, user_id):
    try:
        conn = Connection(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        sql = f"UPDATE user SET password = '{new_psw}' WHERE id = {user_id}"
        conn.execute_query(sql=sql)
        conn.commit()
        conn.disconnect()
    except Exception as err:
        print("Something happend...\n", err)


# dt = get_user_mail_psw("ibrahimplayer23@gmail.com", "barza123")
# print(dt[0])
