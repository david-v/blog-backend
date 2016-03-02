from django.conf.urls import url

from . import controller

app_name = 'blog'
urlpatterns = [
    url(r'^posts$', controller.get_all_posts),
    url(r'^posts/(?P<post_id>[0-9]+)/comment$', controller.add_comment_to_post),
]