import sqlite3
import random
from pprint import pprint

def create_table():
    conn = sqlite3.connect('tasks.db') # create db if ones not made

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY autoincrement NOT NULL,
        user TEXT,
        task TEXT,
        startdate TEXT,
        finishdate TEXT,
        completed INTEGER,
        winner INTEGER,
        winning_date TEXT,
        old INTEGER
        )""")

    conn.commit() #commit the action
    conn.close() #close db after action

def new_task(user, task, startdate, finishdate, completed, winner, winning_date, old):
    conn = sqlite3.connect('tasks.db') # create db if ones not made
    c = conn.cursor()
    
    try: # Try to insert the new task
        c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (None, user, task, startdate, finishdate, completed, winner, winning_date, old))

    except Exception as e:
        print('Inserting into database failed')
        print(e)
        pass

    else:
        print('Added new task to database successfully')

    
    conn.commit()
    conn.close()

def get_all():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute("SELECT id, user, task, startdate, finishdate, completed, winner, winning_date, old FROM tasks")
    results = c.fetchall()

    conn.commit()
    conn.close()
    return results

def get_active(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT id, user, task, startdate, finishdate FROM tasks WHERE completed = ? AND user = ? AND old = 0", (0,(user)))
    results = c.fetchall()

    conn.commit()
    conn.close()
    return results

def get_active_count(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT count(*) FROM tasks WHERE completed = ? AND user = ? AND old = 0", (0,(user)))
    thecount = c.fetchone()

    conn.commit()
    conn.close()
    return thecount

def get_all_active():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute("SELECT id, user, task, startdate, finishdate FROM tasks WHERE completed = ? AND old = 0 ", (0,))
    results = c.fetchall()

    conn.commit()
    conn.close()
    return results

def get_all_active_count():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT user, count(*) as task_count FROM tasks WHERE completed=? AND old = 0 GROUP BY user", (0,))
    thecount = c.fetchall()

    conn.commit()
    conn.close()
    return thecount

def get_completed(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT id, user, task, startdate, finishdate FROM tasks WHERE completed = ? AND user = ? AND old = 0", (1,(user)))
    results = c.fetchall()

    conn.commit()
    conn.close()
    return results

def get_old_completed(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT id, user, task, startdate, finishdate FROM tasks WHERE completed = ? AND user = ? AND old = 1", (1,(user)))
    results = c.fetchall()

    conn.commit()
    conn.close()
    return results

def get_completed_count(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT count(*) FROM tasks WHERE completed = ? AND user = ? AND old = 0", (1,(user)))
    thecount = c.fetchone()

    conn.commit()
    conn.close()
    return thecount

def get_old_completed_count(user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT count(*) FROM tasks WHERE completed = ? AND user = ? AND old = 1", (1,(user)))
    thecount = c.fetchone()

    conn.commit()
    conn.close()
    return thecount

def get_all_completed():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("SELECT id, user, task, startdate, finishdate FROM tasks WHERE completed = ? AND old = 0", (1,))
        results = c.fetchall()
    except Exception as e:
        print(e)
    else:
        print(results)
        conn.commit()
        conn.close()

    return results

def get_all_old_completed():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("SELECT id, user, task, startdate, finishdate, completed, winner, winning_date FROM tasks WHERE completed = ? AND old = 1", (1,0,))
        results = c.fetchall()
    except Exception as e:
        print(e)
    else:
        print(results)
        conn.commit()
        conn.close()

    return results

def get_all_completed_count():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT user, count(*) as task_count FROM tasks WHERE completed=? AND old = 0 GROUP BY user", (1,))
    thecount = c.fetchall()

    conn.commit()
    conn.close()
    return thecount

def get_all_old_completed_count():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT user, count(*) as task_count FROM tasks WHERE completed=? AND old = 1 GROUP BY user", (1,))
    thecount = c.fetchall()
    print(thecount)
    conn.commit()
    conn.close()
    return thecount

def get_all_old():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("SELECT id, user, task, startdate, finishdate, completed, winner, winning_date FROM tasks WHERE old = 1")
        results = c.fetchall()
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()

    return results

def delete_task(id, user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("DELETE FROM tasks WHERE id=? AND user=?", (id,user))
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

def complete_task(finishdate, id, user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE tasks SET completed =1, finishdate =? WHERE id=? AND user=?", (finishdate,id,user))
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()
        return True

def complete_all_tasks(finishdate, user):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE tasks SET completed =1, finishdate =? WHERE completed=0 AND user=? AND old=0", (finishdate,user))
        howmany = c.rowcount
    except Exception as e:
        print(e)
    else:
        print(howmany)
        conn.commit()
        conn.close()
        return True, howmany

def check_if_complete_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT count(*) FROM tasks WHERE completed = ? AND id = ? ", (1,(id)))

    thecount = c.fetchall()

    conn.commit()
    conn.close()

    return thecount

def top(amt):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT user, count(*) as task_count FROM tasks WHERE completed=? AND old = 0 GROUP BY user ORDER BY count(*) DESC LIMIT ?", (1, amt))
    thecount = c.fetchall()
    print(thecount)

    conn.commit()
    conn.close()

    return thecount

def set_winner(winning_date, id, username):
    try:
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("UPDATE tasks SET winner =1, old=1, winning_date =? WHERE id=? AND user=? AND old=?", (winning_date,id,username,0))
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()

def show_winners():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute(f"SELECT user, task, id, winning_date FROM tasks WHERE winner=?", (1,))
    thecount = c.fetchall()
    print(thecount)

    conn.commit()
    conn.close()

    return thecount

def set_all_old():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE tasks SET old =1 WHERE old=0")
        rows = c.rowcount
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()
        return rows

def set_all_old():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE tasks SET old =1 WHERE old=0")
        rows = c.rowcount
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()
        return rows

def drop_table():
    try:
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS tasks;")
    except Exception as e:
        print(e)
        conn.commit()
        conn.close()
    else:
        print('dropped')
        conn.commit()
        conn.close()
        create_table()
        print('Made new table')
        success = 1
        return success

create_table()