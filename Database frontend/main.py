from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)




# Define connection parameters
user = 'root'
password = 'root' # put the password in a seperate file
host = 'localhost'  # or IP address for remote DB
port = 3306
database = 'olist_store'

# Configure database connection using PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: disable tracking for performance


db = SQLAlchemy()   

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

from sqlalchemy import MetaData

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)


metadata = MetaData()

@app.route('/')
def home():
    #TODO: make the front page .e,i loop through the tables names and make a template for the home page . design of thw website is in learning flask
    with app.app_context(): # gets a list of all the tables in the db
        metadata.reflect(bind=db.engine)
        tables_names = list(metadata.tables.keys())
    
    return render_template('tables.html', tables=tables_names)   

  
@app.route('/tables/<table_displayed>') # creates a page for each table in the db
def tables(table_displayed):
    #TODO: get all the column names in the table
    # return f'<h1>Hello, {table_displayed}!</h1>'
   
    with app.app_context():
        result =  db.session.execute( text(f"SELECT * FROM {table_displayed}") ) # a basic select query
        rows = result.fetchall() # the rows  #TODO: GET all the rows in a table

    return render_template('table_columns.html', columns=result.keys(), rows=rows, table_displayed= table_displayed) #.keys() gets the column names



#TODO: Add the css templates 

   




# this ends the coneection with the db
@app.teardown_appcontext
def close_sessions(exception=None):
    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True)