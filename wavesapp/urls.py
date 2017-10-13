from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^profile_list/(?P<role>\d+)/$', views.profile_list, name='profile_list'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^logout?$',auth_views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
<<<<<<< HEAD
    url(r'^search/$',views.search,name='search'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^reserve/$',views.reserve,name='reserve'),
    url('^', include('django.contrib.auth.urls')),
=======
    url(r'^developers/$',views.developers,name='developers'),
>>>>>>> 4569a97de095f70ba23378a415bb4a579d291d5e
]
