# Import flask dependencies
from operator import mod
from flask import Blueprint, request, jsonify, make_response, render_template, Response
from flask_restful import Resource
from app import rest_api
from .models import *
import json
import decimal
from datetime import timedelta
from .utils import extract,get_client,get_total_bytes,exchange
# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_api = Blueprint('api', __name__)

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@mod_api.route('/redoc')
def redoc():
    return render_template('redoc.html')


class ExtractAPI(Resource):

    def post(self):         
        templated_id = '30'
        templated_id = request.json['templated_id']
        if request.json['template_url'] is not None and request.json['template_url'] != "":
            template_url = request.json['template_url']
            
            results = extract(templated_id,template_url)           
            
            if len(results) > 0:
                resp = results         
                return resp, 201
            else:
                return [], 204
        else:
            resp = {
                "template_id": templated_id,
                "error": ["replace_failed", "not_found_template", "exception"],
                "change_key_list": {}
            }
            return resp, 400
        
class Get_file(Resource):
    def post(self):
        s3 = get_client()        
        id = request.json['templated_id']
        
        if request.json['template_url'] is not None and request.json['template_url'] != "":
            template_url = request.json['template_url']
            print(template_url)
            file = s3.get_object(Bucket='miraie-image-storage-tmp', Key=template_url)
            return Response(
                file['Body'].read(),
                mimetype='image/jpg',
                #mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                headers={"Content-Disposition": "attachment;filename=sample_test1.xlsx"}
            )
        else:
            return [], 400        
        
class ExchangeAPI(Resource):
    
    def post(self):
        output_id = request.json['output_id']
        templated_id = request.json['templated_id']
        template_color = request.json['template_color']        
        if request.json['template_url'] is not None and request.json['template_url'] != "" and request.json['replace_info'] is not None:
            template_url = request.json['template_url']
            replace_info = request.json['replace_info']
            
            results = exchange(output_id,templated_id,template_url,replace_info)   
            
            if len(results) > 0:
                resp = results
                return resp, 201
            else:
                resp = {
                    "output_id": output_id,
                    'templated_id': templated_id,
                    "error": ["saved_failed", "exception"],
                    "report_url": ""
                }
                return resp, 400
        else:
            resp = {
                "output_id": output_id,
                'templated_id': templated_id,
                "error": ["saved_failed", "exception"],
                "report_url": ""
            }
            return resp, 400
        
rest_api.add_resource(ExtractAPI, '/extract-data/')
rest_api.add_resource(Get_file, '/get-file/')
rest_api.add_resource(ExchangeAPI, '/exchange-data/')
