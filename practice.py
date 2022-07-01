from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class TaskList(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  task = db.Column(db.String(255), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  creator = db.Column(db.String(255), nullable=False, default='N/A')
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return 'Task' + str(self.id)

@app.route('/<string:name>/post/<int:id>')
def  hello(name, id):
  return 'Hello, ' + name + ', your id is: ' + str(id )


if __name__ == '__main__':
  app.run(debug=True)