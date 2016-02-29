#Blog - Backend

Web service and personal project intended to:

1. Learn Python's tech stack for web (try Django)
2. Provide a persistence layer to my blog

---

**Tech Stack**

	Python
	Django
    MySQL

**Usage**

1 - Make sure you have Python + pip installed

    python -V
    pip -V

(If you don't, google how to install them)

2 - Configure your DB details (just edit blogbackend/settings.py)

3 - Create DB in your MySQL client.

4 - Create DB schema (tables, etc) from Django models:

	python manage.py migrate

5 - Load the test data

	python manage.py shell

(for now from the console or from your MySQL client)

6 - Run the server

    python manage.py runserver

(If you have missing packages and errors come: resolve them by

    pip install missing-package-name


---

**Daily Logbook**

[Here](LOGBOOK.md)
