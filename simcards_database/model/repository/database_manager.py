import sqlite3

def transaction_manager(sql_command,parameter_list=None,commit=True):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    if parameter_list:
        cursor.execute(sql_command,parameter_list)
    else:
        cursor.execute(sql_command)
    if commit:
        connection.commit()
        result_list = parameter_list
    else:
        result_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return result_list

def creat_database():
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()



    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        number INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT,
        register_data TEXT,
        operator TEXT,
        charge INTEGER
        
        )
        """
    )

    cursor.close()
    connection.close()