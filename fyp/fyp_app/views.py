from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import re
import string
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder     
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier          
from sklearn.model_selection import train_test_split 
from sklearn import preprocessing


@csrf_exempt
def urgency(request):
    if (request.method == 'GET'):
        return HttpResponse('Hello world')
    elif(request.method == 'POST'):
        request_data = JSONParser().parse(request)
        message = request_data["message"]

        # Load the Features saved previously
        vectorizer_word_unigram = pickle.load(
            open('D:/FYP/saqib-fyp-app/fyp/fyp_app/urgency model/urgency_vectorizer_word_unigram.pkl', 'rb'))

        unseen_data = pd.DataFrame([(message)],columns=["tweets"])
        unseen_data = unseen_data["tweets"]
        # unseen_data = message
        # Transform the Features of Unseen Data using using the Loaded Vectorizer
        transform_unseen_data = vectorizer_word_unigram.transform(unseen_data)

        transform_unseen_data = transform_unseen_data.todense()
        word_unigram_features = vectorizer_word_unigram.get_feature_names()
        unseen_data_features = pd.DataFrame(transform_unseen_data,
                                            columns=word_unigram_features)
        trained_model = pickle.load(
            open('D:/FYP/saqib-fyp-app/fyp/fyp_app/urgency model/rf_urgency_trained_model.pkl','rb'))
        predicted_Label = trained_model.predict(unseen_data_features)
        
        Prediction = ""
        if predicted_Label == 1:
            Prediction = "Urgent"
        else:
            Prediction = "Not-Urgent"

    # print(request_data["message"])
    result = {"message": message, "prediction": Prediction}
    return JsonResponse(result, status=status.HTTP_200_OK)
    # return HttpResponse('Hello world')

@csrf_exempt
def sentiment(request):
    if (request.method == 'GET'):
        return HttpResponse('Hello world')
    elif(request.method == 'POST'):
        request_data = JSONParser().parse(request)
        message = request_data["message"]

        # Load the Features saved previously
        vectorizer_word_unigram = pickle.load(open('C:/Users/Saqib Ali/Sentiment-vectorizer_word_unigram.pkl', 'rb'))

        unseen_data = pd.DataFrame([(message)],columns=["SentimentText"])
        unseen_data = unseen_data["SentimentText"]
        # Transform the Features of Unseen Data using using the Loaded Vectorizer
        transform_unseen_data = vectorizer_word_unigram.transform(unseen_data)

        transform_unseen_data = transform_unseen_data.todense()
        word_unigram_features = vectorizer_word_unigram.get_feature_names()
        unseen_data_features = pd.DataFrame(transform_unseen_data,
        columns = word_unigram_features)
        # Load the Saved Model
        trained_model = pickle.load(open('D:/FYP/NLP-Deployment-Heroku/rf_Sentiment-trained_model.pkl','rb'))
        # Predict the Label on Unseen Data
        predicted_Label = trained_model.predict(unseen_data_features)
        if predicted_Label == 1:
                Prediction = "Positive"
        else:
                Prediction = "Negative"

        result = {"message": message, "prediction": Prediction}
        return JsonResponse(result, status=status.HTTP_200_OK)
