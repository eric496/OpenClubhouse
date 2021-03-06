from cache import channelsCache
from flask import Blueprint, current_app, jsonify, render_template

bp = Blueprint("clubhouse", __name__)


@bp.route("/")
def index():
    return render_template("index.html", owner_user_id=current_app.config['OWNER_USER_ID'])


@bp.route("/api/getChannels")
def getChannels():
    rooms, channels = channelsCache.get()
    current_app.logger.info(f"len of channels = {len(channels)}")
    return jsonify(channels)


@bp.route("/room/<string:room>")
def join(room):
    return render_template("channel.html", owner_user_id=current_app.config['OWNER_USER_ID'])


@bp.route("/api/room/<string:room>")
def getChannel(room):
    rooms, channels = channelsCache.get()
    if room in rooms and rooms[room]['channel']['joined'] is True:
        return rooms[room]
    return jsonify(None)


# @bp.route("/test")
# def test():
#     return render_template("channel.html", owner_user_id=current_app.config['OWNER_USER_ID'])
