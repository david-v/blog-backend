**Daily logbook**

*29 Feb*

I was planning to write a simple backend for my blog. It needs to persist the 'comments' that people submit to posts. More importantly, it needs to scrape my Github repositories for logbook entries and make posts out of them. I was planning to use **nodejs + MongoDB** but my hosting doesn't support either (and it's paid until 2018). Plan B was to try a new PHP framework but just before I started, I realised that there's a 3rd option which my hosting supports: **Python**!

Until today, I had only ever written 1 Python script to find all 8000 towns in Spain from Wikipedia. This time I want to try the popular **Django**. It'd be great to use Mongo for persistence, but again my hosting doesn't support it so I'll have to stick to MySQL for now.

Django's tutorial is pretty awesome, and I strongly recommend anyone to follow it, it's less than 1h in total, and you realise of what a fantastic framework it is.

It's remarkable that their templating engine is basically Twig (to be fair from what I've read it's the other way around) - which I used for years when doing Symfony. I hate using PHP for templating, and I'm glad Python's approach is the same.

Also, their strong ORM, powerful migrations system -just like Symfony's!- make Django truly sexy to me. This is gonna be fun.
