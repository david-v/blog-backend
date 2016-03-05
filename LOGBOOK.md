#Daily logbook

####Unchaining Django

######29 Feb 2016

I was planning to write a simple backend for my blog. It needs to persist the 'comments' that people submit to posts. More importantly, it needs to scrape my Github repositories for logbook entries and make posts out of them. I was planning to use **nodejs + MongoDB** but my hosting doesn't support either (and it's paid until 2018). Plan B was to try a new PHP framework but just before I started, I realised that there's a 3rd option which my hosting supports: **Python**!

Until today, I had only ever written 1 Python script to find all 8000 towns in Spain from Wikipedia. This time I want to try the popular **Django**. It'd be great to use Mongo for persistence, but again my hosting doesn't support it so I'll have to stick to MySQL for now.

Django's tutorial is pretty awesome, and I strongly recommend anyone to follow it, it's less than 1h in total, and you realise of what a fantastic framework it is.

It's remarkable that their templating engine is basically Twig (to be fair from what I've read it's the other way around) - which I used for years when doing Symfony. I hate using PHP for templating, and I'm glad Python's approach is the same.

Also, their strong ORM, powerful migrations system -just like Symfony's!- make Django truly sexy to me. This is gonna be fun.

> Blog, Python, Django, MySQL, Justhost

---

####Django's admin panel: so cool!

######1 Mar 2016

Of all the frameworks I have tried, Django's automatically generated admin panel is the nicest. CakePHP is okay too, but the way Django handle's user, groups, permissions, in such an editable way is brilliant. For the standard project that needs a backend with different tiers of admin users, Django is perfect.

Anyway, I've written the simple backend that my blog will need in order to get the posts, and send comments to entries. 

> Blog, Python, Django

---

####CORS + CSRF nightmare

######2 Mar 2016

With my Python's web service ready (in localhost:8000 for now), it was time to integrate with my blog's Angular frontend (in localhost:80). The problem comes when they obviously don't share the same hostname. Not a big deal, I set the CORS headers to allow my origin. The problem then was that since I was posting comments from Angular using Content-Type = 'application/json', the browser detects it as a 'non-conventional' post request, so it asks to the server for permission. AKA: it sends a preflight call to the same endpoint it is about to POST, with method=OPTIONS. I had to make my endpoint return with a 200 OK for this special 

Then I had to face the next issue: CSRF validations. That required me to make changes in my frontend, adding it a cookie interceptor, so when it performs the first call: 'GET /posts' it catches the csrf token and sets it as a header in the 'POST /comment' endpoint.

It took me longer than I expected and I read Mozilla's full documentation about HTTP, but finally client-server, Angular-Django's integration is ready!

> CORS, CSRF, Blog, Python, Django, Angular, JS

---

####Django running in Justhost

######3 Mar 2016

Time to deploy my blog's backend to Justhost. Again facing issues here: I had used Django 1.9 which has no longer got support for FastCGI, which seems to be the only way to route Apache to Python's interpreter.

So I had to downgrade to Django 1.6, which means also downgrading my Python from 3.5 to 2.7. Eventually, the deployment is ready, and Django's my web service is live: [api.veli.la/blog/posts](http://api.veli.la/blog/posts)

A million thanks to this guide which helped me massively to setup the whole thing: [http://flailingmonkey.com/install-django-justhost/](http://flailingmonkey.com/install-django-justhost/)

> Blog, Web Service, Django, Python, Justhost, FastCGI, Apache

---

####Github's repos scraper

######4 Mar 2016

Now that my blog's backend and frontend are connected in their live versions: [david.veli.la/blog](http://david.veli.la/blog) I need to make the scraper that will populate my blog with contents from my LOGBOOK.md files from my Github repositories. After I wrote in Python the scraper for wikipedia's information on Spanish towns, this isn't a difficult task at all. Just some XPath magic and my databases are populated!

My blog's ready! From now on, every time I work on personal projects that I put on Github, I won't have to do anything and my blog will start posting these notes in a nice modern format thanks to Angular and Modernizer.

> Python, Scraper, Blog, Github

