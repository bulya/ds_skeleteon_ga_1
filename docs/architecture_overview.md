# ds_skeleteon_ga_1: Architecture overview #

We user [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to run all application components and backing services in isolated environment.

## Software versions ##

* Python **[3.13](https://docs.python.org/)**, installed via [pyenv](https://github.com/pyenv/pyenv).
* Django **[latest stable](https://docs.djangoproject.com/)**, installed via [pip](https://pypi.python.org/pypi) - official Python package index.
* Celery **[latest stable](http://docs.celeryproject.org/en/latest/index.html)**, installed via [pip](https://pypi.python.org/pypi) - official Python package index.
* Postgres **[16.3](https://www.postgresql.org/docs/16.3/static/index.html)**, installed via [official Docker image](https://hub.docker.com/_/postgres).
* Redis **[7.2](https://redis.io/)**, installed via [official Docker image](https://hub.docker.com/_/redis).

## Postgres databases ##

| DB name | Description | Owner |
| ------- | ----------- | ----- |
| `ds_skeleteon_ga_1_db` | database for main application | `postgres` |

## Redis databases ##

| DB number | Usage |
| --------- | ----- |
| `0` | Not used |
| `1` | Celery broker |
| `2` | Direct usage with [`redis_client`](./api/ds_skeleteon_ga_1/apps/common/utils/redis.py#L9) function in main application |
| `3` - `15` | Not used |
