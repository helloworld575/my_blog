from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^article-column/$', views.article_column, name="article_column"),
    url(r'^del-column/$',views.del_column,name="del_column"),
    url(r'^rename-column/$',views.rename_column,name="rename_column"),
    url(r'^article-post/$',views.article_post,name="article_post"),
    url(r'^article-list/$',views.article_list,name="article_list"),
    url(r'^article-detail/(?P<article_id>\d+)/(?P<slug>[-\w]+)/$',views.article_detail,name="article_detail"),
    url(r'^del-article/$',views.del_article,name="del_article"),
    url(r'^edit-article/(?P<article_id>\d+)/$',views.edit_article,name="redit_article"),
]