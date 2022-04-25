from flask import request, Flask
# from flask_sqlalchemy import SQLAlchemy
from app import app
from app.models import UniqueIDs
from app.database import session


# from app.boto3_service import boto3_aws_client, upload_file, read_image_from_s3, delete_image_from_s3
# from app.utils.get_auth_header import get_auth_header
# from app.utils.http_error_handler import http_error_handler
# from app.utils.check_if_valid_schema import check_if_valid_schema


import json
import uuid



@app.route('/api/uuid', methods=['GET'])
def generate_uuid():
    """
    Generates a new UUID for the user
    """
    # for(key, value) in request.headers.items():
    #     print(key, value)
    
    useragent = str(request.headers.get('User-Agent'))

    myuuid = str(uuid.uuid4())
    return json.dumps({'uuid': myuuid, 'useragent': useragent}), 201


@app.route('/api/uuid', methods=['POST'])
def generate_uuid_post():
    """
    Generates a new UUID for the user and saves it in DB
    """
    # for(key, value) in request.headers.items():
    #     print(key, value)
    if(request.form.get('generate') == "1"):
        # print("hello")
        
        useragent = str(request.headers.get('User-Agent'))

        #generate uuid
        myuuid = str(uuid.uuid4())


        # checking if user already exists
        # if the uuid exists - generate new one 
        while UniqueIDs.query.filter_by(uuid=myuuid).first() is not None:
            myuuid = str(uuid.uuid4())
        
        # save uuid to db
        new_uuid = UniqueIDs(uuid=myuuid, useragent=useragent)
        session.add(new_uuid)
        session.commit()
        
        return json.dumps({'uuid': myuuid, 'saved_to_db': "yes"}), 201
    else:
        return json.dumps({'saved_to_db': "no"}), 201



@app.route('/view')
def view():
    # fetches all the uuids saved
    uuids = UniqueIDs.query.all()
    # response list consisting user details
    response = list()
 
    for uuid in uuids:
        response.append({
            'id': uuid.id,
            'uuid': uuid.uuid,
            'useragent': uuid.useragent
        })
    return json.dumps({
        'status' : 'success',
        'message': response
    }), 200



# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port="8080")
