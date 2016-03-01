from django.conf.urls import url

from . import controller

app_name = 'blog'
urlpatterns = [
    # ex: /blog/posts
    url(r'^posts$', controller.get_all_posts, name='get_all_posts'),
    # ex: /blog/posts/5/comment
    url(r'^posts/(?P<post_id>[0-9]+)/comment$', controller.add_comment_to_post, name='add_comment_to_post'),
]