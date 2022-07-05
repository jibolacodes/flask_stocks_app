from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#       -----DATABASE-----
# states where database is stored
# sqlite is only used for development mode
# For production mode, you can use another
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# Designing the database
class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(20), nullable=False, default='N/A')
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return 'Blog Post' + str(self.id)

# Using templates for the UI
@app.route('/')
def index():
  return render_template('index.html')

# Passing data to webpages
# ===============================================
#                 #CRUD
# ===============================================
# a.Read
@app.route('/posts', methods=['GET', 'POST'])
def posts():

  if request.method == 'POST':
    return redirect('/posts')
  else:
    # getting the items of BlogPost
    all_posts = BlogPost.query.all()
    return render_template('posts.html', posts=all_posts)
    
# b. Edit
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
  post = BlogPost.query.get_or_404(id)
  
  if request.method == 'POST':
    post.title = request.form['title']
    post.author = request.form['author']
    post.content = request.form['content']
    db.session.commit()
    return redirect('/posts')
  else:
      return render_template('edit.html', post=post)

# c. Delete
@app.route('/posts/delete/<int:id>')
def delete(id):
  post = BlogPost.query.get_or_404(id)
  db.session.delete(post)
  db.session.commit()
  return redirect('/posts')

@app.route('/posts/write', methods=['GET', 'POST'])
def write():
  if request.method == 'POST':
    post_title = request.form['title']
    post_author = request.form['author']
    post_content = request.form['content']
    new_post = BlogPost(title=post_title, content=post_content, author=post_author)
    # add new_post to the database
    db.session.add(new_post)
    # commit to the database
    db.session.commit()
    # redirect to same page which shows the new_post
    return redirect('/posts')
  else:
      return render_template('write.html')



if __name__ == "__main__":
  app.run(debug=True) 