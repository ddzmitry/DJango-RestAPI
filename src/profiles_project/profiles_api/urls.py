from  django.conf.urls import url
# for viewSet
from django.conf.urls import include
#  Default rooter is important
from rest_framework.routers import DefaultRouter 
# 
from . import views
router = DefaultRouter()
# register new url 
router.register('hello-viewset',views.HelloViewSet, base_name ='hello-viewset')
# register UserProfiles
router.register('profile', views.UserProfileViewSet)
# reguster login rooter
router.register('login', views.LoginViewSet, base_name='login')
# describe url
urlpatterns = [
    # as_view is very importannt to be able to send actual JSON object
    url(r'^hello-view/', views.HelloApiView.as_view()),
    # this is how we use viewset because router will map itself to proper url
    url(r'', include(router.urls))
]