from .sql_practice.sql_learning import SQLExecution



def sql_execute(name, password):
    sql_obj = SQLExecution()
    conn = sql_obj.connect_with_server("localhost", "root", "0599", "mydb")
    query = f"INSERT INTO user_info (name, pwds) VALUES ('{name}', '{password}');"
    res, msg = sql_obj.execute_query(conn, query)
    return msg
