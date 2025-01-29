from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    return HttpResponse("Shinomiyaa ( •̀ ω •́ )✧")


class DRFAPIView(APIView):
    def get(self, request):
        return Response("Shinomiyaa ( •̀ ω •́ )✧")
