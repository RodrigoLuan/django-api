import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from cfeapi.mixins import JsonResponseMixin
from .models import Update
# Create your views here.
#def detial_view(request):
    #return render() #return json data XML
    #return HttpResponse(get_template().render({}))

def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj= Update.objects.get(id=1)
        data = serialize("json", [obj,], fields=('user', 'content'))
        json_data = data
       # data = {
       #     "user": obj.user.username,
       #     "content": obj.content
       # }
       # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        #data = serialize("json", qs, fields=('user', 'content'))
        #print(data)
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')