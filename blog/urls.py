from django.conf.urls import patterns, url
from . import controller

urlpatterns = patterns('',
    url(r'^posts$', controller.get_all_posts),
    url(r'^posts/(?P<post_id>[0-9]+)/comment$', controller.add_comment_to_post),
)
