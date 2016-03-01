from django.http import HttpResponse
import json

from .models import Post, Comment


def get_all_posts(request):
    posts = Post.objects.filter(published=True).prefetch_related('comments').order_by('-createdOn')
    data = []
    for post in posts:
        data.append(post.serialize())
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response['Access-Control-Allow-Credentials'] = 'true'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    response['Access-Control-Allow-Origin'] = 'http://localhost'
    return response


def add_comment_to_post(request, post_id):
    response = HttpResponse(content_type="application/json")
    response['Access-Control-Allow-Origin'] = 'http://localhost'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'X-CSRFToken, Content-Type'
    response['Access-Control-Allow-Credentials'] = 'true'
    if request.method == 'OPTIONS':
        response.status = 200
    elif request.method == 'POST':
        try:
            post = Post.objects.get(pk=post_id)
            json_body = json.loads(request.body)
            comment_body = json_body['body']
            comment_author = json_body['author']
            Comment.objects.create(post=post, author=comment_author, body=comment_body)
            response.status = 201
        except Post.DoesNotExist:
            response.status = 404
    else:
        response.status = 405

    return response

