from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post, Comment
import project.settings
from .scraper import scrape_all_repos


def get_all_posts(request):
    response = HttpResponse(content_type="application/json")
    response['Access-Control-Allow-Origin'] = project.settings.FRONTEND_URL
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    response['Access-Control-Allow-Credentials'] = 'true'

    if request.method != 'GET':
        response.status_code = 405
        return response

    posts = Post.objects.filter(published=True).prefetch_related('comments').order_by('-created_on')
    data = []
    for post in posts:
        data.append(post.serialize())

    response.write(json.dumps(data))
    response.status_code = 200
    return response


@csrf_exempt
def add_comment_to_post(request, post_id):
    response = HttpResponse(content_type="application/json")
    response['Access-Control-Allow-Origin'] = project.settings.FRONTEND_URL
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

    try:
        comment_captcha = json_body['captcha']
        comment_body = json_body['body']
        comment_author = json_body['author']
    except KeyError:
        response.status_code = 406
        return response

    if comment_captcha != (post.id % 8):
        response.status_code = 418
        return response

    Comment.objects.create(post=post, author=comment_author, body=comment_body)
    response.status_code = 201
    return response


def run_scraper(request):
    posts = scrape_all_repos()
    return HttpResponse(json.dumps(posts), content_type="application/json")
