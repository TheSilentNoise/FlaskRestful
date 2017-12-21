from flask import Flask,jsonify
from flask_restful import Resource, Api,reqparse
from flaskext.mysql import MySQL
from dbase import db

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = str(db.MYSQL_DATABASE_USER)
app.config['MYSQL_DATABASE_PASSWORD'] = str(db.MYSQL_DATABASE_PASSWORD)
app.config['MYSQL_DATABASE_DB'] = str(db.MYSQL_DATABASE_DB)
app.config['MYSQL_DATABASE_HOST'] = str(db.MYSQL_DATABASE_HOST)

mysql.init_app(app)

class CreateUser(Resource):
        def post(self):
            try:
                # Parse the arguments
                parser = reqparse.RequestParser()
                parser.add_argument('email', type=str, help='Email address to create user')
                parser.add_argument('password', type=str, help='Password to create user')
                args = parser.parse_args()

                _userEmail = args['email']
                print (_userEmail)
                _userPassword = args['password']
                print(_userPassword)

                conn = mysql.connect()
                cursor = conn.cursor()
                query = "INSERT INTO tblUser (UserName, Password) VALUES('" + _userEmail + "','" + _userPassword + "');"
                print(query)
                cursor.execute(query)
                conn.commit()

                return {'StatusCode':'200','Message': 'User creation success'}

            except Exception as e:
                return {'error': str(e)}

class GetUser(Resource):
        def get(self,userid):
            #print (userid)

            conn = mysql.connect()
            cursor = conn.cursor()
            query = "SELECT * FROM tblUser WHERE UserId = '" + userid + "';"
            #print(query)
            cursor.execute(query)
           # conn.commit()
            data = cursor.fetchall()
            print(str(data[0][1]))

            return jsonify(data)

class DeleteUser(Resource):
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('userid', type=str, help='Email address to create user')
        args = parser.parse_args()

        _userId = args['userid']

        conn = mysql.connect()
        cursor = conn.cursor()
        query = "DELETE FROM tblUser WHERE UserId = '" + _userId + "';"
        print(query)
        cursor.execute(query)
        conn.commit()
        return "success"

class PutUser(Resource):
    def put(self):

        parser = reqparse.RequestParser()
        parser.add_argument('userid', type=str, help='Email address to create user')
        parser.add_argument('username', type=str, help='Password to create user')
        args = parser.parse_args()

        _userId = args['userid']
        _userName = args['username']

        conn = mysql.connect()
        cursor = conn.cursor()
        query = "UPDATE tblUser SET UserName='"+ _userName +"' WHERE UserId = '"+ _userId +"';"
        print(query)
        cursor.execute(query)
        conn.commit()
        return "Output:success"

api.add_resource(CreateUser, '/CreateUser/')
api.add_resource(GetUser,'/GetUser/<userid>')
api.add_resource(DeleteUser,'/DeleteUser/')
api.add_resource(PutUser,'/PutUser/')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)