import mysql.connector
__connection = None #if the function is called more than once it makes a connection for each call but i only want one connection no matter how many times the connection is called
def get_sql_connection():
    print("Opening mysql connection")
    global __connection
    if __connection is None:
        __connection = mysql.connector.connect(user='root', password='root',
                                            host='127.0.0.1',
                                            database='olist_store')
    return __connection