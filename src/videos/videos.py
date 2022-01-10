# REST API == Representational State Transfer - Application Programming Interface
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Hey you didn't send the name of the video!",
                            required=True)
video_put_args.add_argument("views", type=int, help="Hey you didn't send the number of views the video has!",
                            required=True)
video_put_args.add_argument("likes", type=int, help="Hey you didn't send the number of likes the video has!",
                            required=True)

videos = {}


def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(http_status_code=404, message="Could not find video...")


def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(http_status_code=409, message="Video already exists with that ID...")


# Create a resource, inherit from resource
class HelloWorld(Resource):
    @staticmethod
    def get(self, name):
        return names[name]

# Common practice for methods to match HTTP methods
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return f'Video with video_id: {video_id} deleted successfully!', 204


# Register resource: "/" for default url, "/helloworld" when user types helloworld
# ask for a <string>, <int> or <boolean>
api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # Start server and flask application
    app.run(debug=True)  # in debug mode, use for dev environment not production
