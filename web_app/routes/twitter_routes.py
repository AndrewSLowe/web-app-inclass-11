
from flask import Blueprint, render_template

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    # user_info = {"screen_name": "__", "followers_count": 100}

    return render_template("user.htm", screen_name=screen_name)