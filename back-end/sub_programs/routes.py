from sub_programs import app
from flask import Response, request
import time

@app.route('/back-end', methods = ['POST'])
def time_stamp():
    event = request.get_json()
    timestamp = event["ts"]

    return Response(f" Time stamp is: {str(timestamp)}", mimetype='text/plain')

