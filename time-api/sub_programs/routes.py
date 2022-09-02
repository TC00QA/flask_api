from sub_programs import app
from flask import Response
import time

@app.route('/time_stamp', methods = ['GET'])
def time_stamp():
    return Response(str(time.time()), mimetype='text/plain')

