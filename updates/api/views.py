import json
from django.views.generic import View
from django.http import HttpResponse

from cfeapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin 

from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel


class updateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data, status = 403)




class updateModelListAPIView(CSRFExemptMixin, View, HttpResponseMixin):
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        #print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message":"not allowed"}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message":" You cannot delete an entire list."})
        status_code = 403
        return self.render_to_response(data, status = 403)