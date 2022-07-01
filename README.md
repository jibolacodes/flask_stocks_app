***Installations***
1. Flask : pip install flask
2. Flask-SQLAlchemy : pip install flask-sqlalchemy

***Creating database***
- Ensure you're on the flask project directory then run "python" in terminal.
  *"from app import db"*
  *"db.create_all()"*

***Importing Models***
  *from app import BlogPost*
  <!-- Split all BlogPost content to me in a list -->
  *BlogPost.query.all()*

  <!-- Adding 2 posts to the database -->
  1.  db.session.add(
        BlogPost(
          title='Blog Post 1', 
          content='Content of blog post 1', 
          author='jibolacodes'
        )
      )
      *BlogPost.query.all()*

  2.  db.session.add(
        BlogPost(
          title='Blog Post 2', 
          content='Content of blog post 2'
        )
      )
      *BlogPost.query.all()*

***Checking the content each blog posts***
  <!-- index is either 0 or 1 as the list is zero-indexed. -->
  BlogPost.query.all()[index].content


Filter
BlogPost.query.filter_by(title='First Blog Post!').all()

Order by
.order_by(key)

.get(primary_key_id)
.get_or_404()

Delete
db.session.delete(BlogPost.query.get(primary_key_id))
db.session.commit()