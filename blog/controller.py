from django.http import HttpResponse
import json

from .models import Post, Comment


def get_all_posts(request):
    response = HttpResponse(content_type="application/json")
    response['Access-Control-Allow-Origin'] = 'http://localhost'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    response['Access-Control-Allow-Credentials'] = 'true'

    if request.method != 'GET':
        response.status_code = 405
        return response

    posts = Post.objects.filter(published=True).prefetch_related('comments').order_by('-createdOn')
    data = []
    for post in posts:
        data.append(post.serialize())

    response.write(json.dumps(data))
    response.status_code = 200
    return response


def add_comment_to_post(request, post_id):
    response = HttpResponse(content_type="application/json")
    response['Access-Control-Allow-Origin'] = 'http://localhost'
    response['Access-Control-Allow-Headers'] = 'X-CSRFToken, Content-Type'
    response['Access-Control-Allow-Credentials'] = 'true'
    response['Access-Control-Allow-Methods'] = 'POST'

    if request.method == 'OPTIONS':  # for preflight calls
        response.status = 200
        return response

    if request.method != 'POST':
        response.status_code = 405
        return response

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        response.status_code = 404
        return response

    json_body = json.loads(request.body.decode('utf-8'))

    comment_captcha = json_body['captcha']
    if comment_captcha != (post.id % 8):
        response.status_code = 406
        return response

    comment_body = json_body['body']
    comment_author = json_body['author']
    Comment.objects.create(post=post, author=comment_author, body=comment_body)
    response.status_code = 201
    return response


