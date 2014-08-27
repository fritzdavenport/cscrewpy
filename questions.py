import sqlite3 as sql
import sys
import os
print('sqlite3', sql.version)

try:
    conn = sql.connect('cscrew.db', isolation_level=None);
    c = conn.cursor();
    c.execute('CREATE TABLE IF NOT EXISTS Survey(Name TEXT, Reason TEXT, Email TEXT)')
    while True:
        os.system('clear')
        name = input("\nWhat is your name? Ex. Jane Kapoodle\n");
        why = input("\nWhat is the reason for your visit? Ex. CS008 Homework Help or maybe Working on Project for Project Night\n" );
        email = input("\nWhat is enter your UVM NetID? \n");
        c.execute('INSERT INTO Survey VALUES (?,?,?)', (name, why, email));
        os.system('clear')
        input("Thanks for your time! You are helping us get funding! (Like for pizza and project night) - Hit enter to return\n")
except(e):
    if c:
        c.rollback()
    print("Error %s:" % e.args[0])
    sys.exit(1)
    
finally:
    if c:
        c.close() 