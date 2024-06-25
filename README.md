# Trackr
![Logo](https://i.imghippo.com/files/jvtgz1719339005.png)The all-in-one site for PSHS students to **manage** and **track** their activities, as well as **automatically calculate their subject grades**.
## Features

- [Assignment Tracking]
- [Automatic Scheduling]
- [Collection Templates]
- [Collection Following System]
## Local Installation

NOTE: Before you install the project, you should have [**pipenv**](https://pipenv.pypa.io/en/latest/) and [**Python**](https://www.python.org/downloads/) installed on your machine (which should be included in the default python installation).

To install the project and run the server on your machine:

1. **Clone the repository** on a directory.

```bash
  git clone https://github.com/pjpdorango/Trackr
```

2. Then, **go to the project directory** and **install all of the libraries** with pipenv. The project directory should have a `Pipfile.lock` file containing all of the libraries used (as of now, only Django).

```bash
  cd [PATH]/Trackr
  pipenv sync
```

3. To run the server, run this command:

```bash
  python manage.py runserver
```

The server, on default, will be run on your `8000` port.

### Pipenv Alternative

If the `python manage.py runserver` command does not work, and the issue is relating to the django library not being found, simply **install the django library manually**, either through the [website](https://docs.djangoproject.com/en/5.0/topics/install/) or with pip:

```bash
  pip install django
```


## Developers

- [![@pjpdorango](https://img.shields.io/badge/PJ-blue?logo=github)](https://github.com/pjpdorango)
  - "nyello"
- [![@ndvelasco](https://img.shields.io/badge/Naeema-brown?logo=github)](https://github.com/ndvelasco)
  - [u should put a quote here]

## Acknowledgements

**Need a site to calculate your final grade?** Check out [calc.dantis.me](https://calc.dantis.me), which was a very big inspiration to the site.
