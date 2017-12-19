from flask import Flask,request,render_template
from flask_restful import Resource, Api, request, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'name': 'hello world'},201,{'addheaderTag':'hello Flask'}


class ToDoSimple(Resource):
    def get(self, todo_id):
        return {todo_id : todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        #return {todo_id : todos[todo_id]}

class TaskListAPI(Resource):
    def get(self):
        #return {"testList":"32"}
        headers = {'Content-Type':'text/html'}
        return render_template('static.html'),200,headers

    def post(self):
        pass

class TaskAPI(Resource):

    def get(self,id):
        return {"test":id}

    def put(self,id):
        pass

    def delete(self,id):
        pass

api.add_resource(TaskListAPI,'/todo/api/v1.0/tasks/',endpoint='tasks')
api.add_resource(TaskAPI,'/todo/api/v1.0/tasks/<int:id>',endpoint='task')

api.add_resource(HelloWorld, '/main')
api.add_resource(ToDoSimple, '/<string:todo_id>')

if __name__ == "__main__":
    app.run(debug=True)