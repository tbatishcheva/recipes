from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipes_list, name='recipes_list'),
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
    url(r'^recipe/(?P<pk>[0-9]+)/edit/$', views.recipe_edit, name='recipe_edit'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^author/(?P<pk>[0-9]+)/$', views.author, name='author'),

]