Pomona Research in Mathematics Experience
==============

This is the code for the Pomona Resarch in Mathematics Experience Database website.

Installation
-----------

If you already have Nginx and PostgreSQL installed and configured on your system, you can proceed with the steps below to set up a copy of the website.

```{sh}
git clone https://github.com/prime-db/prime-db.git prime-db
```

#### For Linux users

 * Prepare your Python environment:

```{sh}
apt install python3.10-venv
python -m venv env
. env/bin/activate
```

 * Proceed to install dependencies:

```{sh}
pip install Flask gunicorn python-dotenv psycopg2-binary
```

```
gunicorn --bind 0.0.0.0:57 app:app
```
