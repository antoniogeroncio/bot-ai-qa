#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from allennlp.predictors.predictor import Predictor
from allennlp.models.archival import load_archive

app = Flask(__name__)
api = Api(app)
    
class QuestionAnsweringResource(Resource):
    def post(self):
        question = request.json['question']
        passage = request.json['passage'] 
        print(passage)
        archive = load_archive('https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz')
        predictor = Predictor.from_archive(archive, 'machine-comprehension')
        answering = predictor.predict(question, passage)
        return answering

api.add_resource(QuestionAnsweringResource, '/api/qa')

if __name__ == '__main__':
     app.run()