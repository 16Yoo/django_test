import random
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view

import quiz
from .models import Quiz
from .serializers import QuizSerializer
import random

from quiz import serializers


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")


@api_view(['GET'])
def randomQuiz(request, id):
    totlaQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totlaQuizs),id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)
