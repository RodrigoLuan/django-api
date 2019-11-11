from django.conf.urls import url


from .views import (
          updateModelDetailAPIView,
          updateModelListAPIView
          )

urlpatterns = [

    url(r'^$', updateModelListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', updateModelDetailAPIView.as_view()),

]
