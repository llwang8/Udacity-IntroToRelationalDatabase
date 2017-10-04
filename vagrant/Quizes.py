# Udacity :

# Intro to Relational Database

#===========================================================
# lesson 3:

# Quiz: Trying out DB API
# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#
import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()

# -----------------------------------
# Quiz: Inserts in DB API
# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
#
import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()

# -----------------------------------



#===========================================================
# lesson 4:

# Quiz: Self joins
#
# Roommate Finder v0.9
#
# This query is intended to find pairs of roommates.  It almost works!
# There's something not quite right about it, though.  Find and fix the bug.
QUERY = '''
select a.id, b.id, a.building, a.room
       from residences as a, residences as b
 where a.building = b.building
   and a.room = b.room and a.id < b.id
 order by a.building, a.room;
'''
# To see the complete residences table, uncomment this query and press "Test Run":
#
# QUERY = "select id, building, room from residences;"
# -----------------------------------

# Quiz: Counting What isn't there
# Here are two tables describing bugs found in some programs.
# The "programs" table gives the name of each program and the files
# that it's made of.  The "bugs" table gives the file in which each
# bug was found.
#
# create table programs (
#    name text,
#    filename text
# );
# create table bugs (
#    filename text,
#    description text,
#    id serial primary key
# );
#
# The query below is intended to count the number of bugs in each
# program. But it doesn't return a row for any program that has zero
# bugs. Try running it as it is.  Then change it so that the results
# will also include rows for the programs with no bugs.  These rows
# should have a 0 in the "bugs" column.
"""
select programs.name, count(bugs.id) as num
   from programs left join bugs
        on programs.filename = bugs.filename
   group by programs.name
   order by num;
"""
# -----------------------------------

# Quiz: One query not two
# Find the players whose weight is less than the average.
#
# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.
#

def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    #cursor.execute("select avg(weight) as av from players;")
    #av = cursor.fetchall()[0][0]  # first column of first (and only) row
    cursor.execute("select name, weight from players, (select avg(weight) as av from players) as subq where weight < av; ")
    return cursor.fetchall()
# -----------------------------------


