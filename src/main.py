# REST API == Representational State Transfer - Application Programming Interface
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Create a resource, inherit from resource
class HelloWorld(Resource):
    def get(self, name, test_num):
        silly_dict = {"name": f"Hello World and {name}", "test_num": test_num}
        return silly_dict

    def post(self):
        return {"data": "Postid"}


# Register resource: "/" for default url, "/helloworld" when user types helloworld
# ask for a <string>, <int> or <boolean>
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test_num>")


if __name__ == "__main__":
    # Start server and flask application
    app.run(debug=True)  # in debug mode, use for dev environment not production
