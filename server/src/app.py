import os
from flask import Flask
from flask_cors import CORS

import datatables.database as db
from routes.exampleRoutes import exampleBlueprint

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
#    os.getenv('DB_USER', 'flask'),
#    os.getenv('DB_PASSWORD', ''),   
#    os.getenv('DB_HOST', 'mysql'),
#    os.getenv('DB_NAME', 'flask')
#)

#db.init_app(app)

db.init_database()
db.engine_start_func()
db.create_tables()

CORS(app, resources={r'/*': {'origins': '*'}})

app.register_blueprint(exampleBlueprint)

if __name__ == '__main__':
    app.run()