# "Database code" for the DB Forum.

import datetime, psycopg2, bleach

dbname = 'forum'

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts_org():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post_org(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))

# get posts from database
def get_posts():
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  c.execute("UPDATE posts SET content = 'cheese' where content like '%spam%'")
  db.commit()
  c.execute("DELETE from posts where content like '%cheese%'")
  db.commit()
  c.execute("SELECT content, time FROM posts ORDER BY time DESC")
  #posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
  posts = c.fetchall()
  db.close()
  return posts

# add a post to the database
def add_post(content):
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  #c.execute("INSERT INTO posts VALUES ('%s') % content")
  #c.execute("INSERT INTO posts VALUES (%s)", (content,))
  c.execute("insert into posts values (%s)", (bleach.clean(content),))
  db.commit()
  db.close()

def UpdatePost():
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  c.execute("UPDATE posts SET content = 'cheese' where content like '%spam%'")
  db.commit()
  db.close()

def DeletePost():
  db = psycopg2.connect(database=dbname)
  c = db.cursor()
  c.execute("DELETE from posts where content like '%cheese%'")
  db.commit()
  db.close()





