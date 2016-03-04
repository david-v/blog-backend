from datetime import datetime
import pytz as pytz
import requests
from .models import Repo, Post
from lxml import html, etree
from dateutil import parser


def scrape_all_repos():
    repos = Repo.objects.filter(enabled=True)
    for repo in repos:
        scrape_repo(repo)

    return 'ok'


def scrape_repo(repo):
    print('SCRAPING: ' + repo.logbook_url)
    page = requests.get(repo.logbook_url)
    if page.status_code != 200:
        print('Error ' + page.status_code + ' scraping ' + repo.logbook_url)
        return False
    tree = html.fromstring(page.content)
    element = tree.xpath('//*[@id="readme"]/article')[0]

    new_post = True
    posts = []
    post = Post()

    for child in element.getchildren():
        if child.tag == 'h1':
            continue
        elif child.tag == 'h4' and new_post:
            post = Post()
            new_post = False
            post.title = child.text
            post.published = False
            post.body = ''
        elif child.tag == 'h6':
            subtag = child.getchildren()[0]
            if subtag.tag == 'a':
                post.created_on = parser.parse(child.text)
                post.tags = repo.name
        elif child.tag == 'p':
            body_string = etree.tostring(child, encoding='utf8', method='xml')
            post.body += body_string.decode("utf-8")
        elif child.tag == 'blockquote':
            subtag = child.getchildren()[0]
            if subtag.tag == 'p':
                post.tags = subtag.text
        elif child.tag == 'hr' and not new_post:
            new_post = True
            posts.append(post)

    if not new_post:
        posts.append(post)

    for post_scraped in posts:
        post_scrape_date = post_scraped.created_on.replace(tzinfo=pytz.UTC)
        if post_scrape_date > repo.last_scraped:
            post_scraped.save()

    now = datetime.utcnow()
    now_aware = now.replace(tzinfo=pytz.utc)
    repo.last_scraped = now_aware
    repo.save()
