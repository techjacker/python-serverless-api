from flask import Blueprint
from flask import request, jsonify

from .errors import error_message

api = Blueprint('api', __name__)


@api.app_errorhandler(404)
def handle404(error=None):
    return error_message(404, 'Not found url {}'.format(request.url))


@api.app_errorhandler(405)
def handle405(error=None):
    return error_message(405, 'Method not supported')


@api.app_errorhandler(500)
def handle500(error=None):
    return error_message(500, 'Something went wrong')


@api.route('/healthz', methods=('HEAD', 'GET'))
def handle_healthcheck():
    return 'ok'


@api.route('/artists', methods=('GET', 'POST'))
def handle_artists():
    """
    handle_artists handles /artists route
    returns list of artists
    """
    if request.method == 'POST':
        return 'ok'

    return jsonify([{'name': 'enya'}])
