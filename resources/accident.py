from flask import jsonify,make_response
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from AccidentPredictor import *

class Accident(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('dow',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('rt',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('sl',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('wc',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('lc',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('rsc',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")

    def post(self):
        data = Accident.parser.parse_args()
        pdf=DataFrame(
                        {
                            'Day_of_Week':[data['dow']],
                            'Road_Type':[data['rt']],
                            'Speed_limit':[data['sl']],
                            'Weather_Conditions':[data['wc']],
                            'Light_Conditions':[data['lc']],
                            'Road_Surface_Conditions':[data['rsc']]
                        }
                    )
        pred=int(nbmodel.predict(pdf)[0])
        acc=round(float(nbknnaccuracy*100),2)
        return make_response(jsonify({'prediction':pred,'accuracy':acc}), 200)
