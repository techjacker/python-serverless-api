from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_message(code, message):
    """
    error_message wraps an error into payload format expected by the API client
    """
    return jsonify({
        'error': {
            'code': HTTP_STATUS_CODES.get(code, code),
            'message': message
        }
    }), code


def unprocessable_entity(errors):
    """
    :param errors:
    :type errors: dict of (string, list or str)
        {
          "artist": [
            "Should be existing artist."
          ],
          "isrc": [
            "Missing data for required field."
          ]
        }
    :return:
    """
    pair = list(errors.items())[0]
    message = 'Key {}. {}'.format(pair[0], ' '.join(pair[1]))
    return error_message(422, message)
