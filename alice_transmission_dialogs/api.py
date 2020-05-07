#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import argparse
import os
import sys
import alice_transmission_dialogs.libs.tools as tools
from flask import Flask, request
from alice_transmission_dialogs.libs.transmission import Transmission

app = Flask(__name__)
transmission = None
logger = None


@app.route("/transmission", methods=['POST'])
def api():
    global logger
    logger.debug('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)
    logger.debug('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


def handle_dialog(req, res):
    global transmission
    if any(elem in ['скачивается', 'активно'] for elem in req['request']['nlu']['tokens']):
        res['response']['text'] = transmission.get_active_torrent()
        return
    else:
        res['response']['text'] = 'Я вас не поняла. Попробуйте повторить запрос.'


def cli():
    parser = argparse.ArgumentParser(description='Alice Transmission Dialog')
    parser.add_argument('--tr-address', default=os.environ.get('TR_ADDRESS', 'transmission.local'), help='Transmission client address', metavar='string')
    parser.add_argument('--tr-port', default=os.environ.get('TR_PORT', '9091'), help='Transmission client port', metavar='string')
    parser.add_argument('--tr-username', default=os.environ.get('TR_USERNAME', 'admin'), help='Username for transmission client', metavar='string')
    parser.add_argument('--tr-password', default=os.environ.get('TR_PASSWORD', 'password'), help='Password for transmission client', metavar='string')
    parser.add_argument('--debug', default=os.environ.get('TR_DEBUG', False), action='store_true', help='Enable debug level logging')
    return parser.parse_args()


def main():
    global logger
    global transmission
    args = cli()
    logger = tools.init_log(debug=args.debug)
    try:
        transmission = Transmission(address=args.tr_address,
                                    port=args.tr_port,
                                    user=args.tr_username,
                                    password=args.tr_password
                                    )
    except Exception as exc:
        logger.error('Transmission connection error: {}'.format(exc))
        sys.exit(1)
    app.run(debug=False, host='0.0.0.0')


if __name__ == '__main__':
    main()
