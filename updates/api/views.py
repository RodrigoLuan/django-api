from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel


class updateModelDetailAPIView(View):
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')#json #httpresponse

    def post(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')




class updateModelListAPIView(View):
    def render_to_response(data, status = 200):
        return HttpResponse(data, content_type='application/json', status=status)

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        data = json.dumps({"message":"Unknown data."})
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message":" You cannot delete an entire list."})
        status_code = 403
        return self.render_to_response(data, status = 403)