from  django.conf.urls import url
from . import views

# describe url
urlpatterns = [
    # as_view is very importannt to be able to send actual JSON object
    url(r'^hello-view/', views.HelloApiView.as_view()),

]