#!/usr/bin/python3
"""
takes an argument and matches name with the said
argument
in states.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    lst = cur.fetchall()
    for r in lst:
        if r[1] == argv[4]:
            print(r)
    cur.close()
    db.close()
