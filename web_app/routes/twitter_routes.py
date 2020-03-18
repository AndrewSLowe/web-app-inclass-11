
from flask import Blueprint, render_template

twitter_routes = Blueprint("twitter_routes", __name__)

@home_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    # user_info = {"screen_name": "__", "followers_count": 100}
    user_info = api.get_user(screen_name)

    return jsonify(user_info)