#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""
from flask import Flask, jsonify, abort, make_response
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse, fields, marshal
from SendCode import hello


app = Flask(__name__, static_url_path="")
api = Api(app)
"""auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)
"""
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TaskListAPI(Resource):
   # decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': [marshal(task, task_fields) for task in tasks]}

    """def post(self):
        args = self.reqparse.parse_args()
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        tasks.append(task)
        #hello(title)
        return {'task': marshal(task, task_fields)}, 201"""


class TaskAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, command):
        """task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        hello(command)
	return {'result':True}"""
	return{'Error':True}

    """def put(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}"""
    def post(self, command):
        """task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        print("In Post")"""
        print('Passed command: '+command)
        hello(command)
        return {'result': True}


api.add_resource(TaskListAPI, '/todo/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/task/<string:command>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=False)
