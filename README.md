# HURUmap

HURUmap is an interactive web platform that allows citizens and journalists to explore, visualise, and download census data. This gives them the power to give context to stories that was otherwise hard to spot. Accessible at https://hurumap.org

### Goals

Instead of re-inventing the wheel, HURUmap relies on the excellent [Wazimap](https://github.com/OpenUpSA/wazimap) and Census Reporter projects and aims to do the following:

1. Extend the features available e.g download SVG / PNG
2. Provide a platform of shared data - tables and geographies (using mapit) that can be re-used with the different apps
3. Provide shared styling, design, attribution, and other engagement content preferences

## Usage

TODO: How to build HURUmap-powered apps using opinionated Docker.

### Install HURUmap Django App / package 

1. Install the package

    ```
    pip install -e git+https://github.com/CodeForAfrica/HURUmap.git@master#egg=hurumap

    ```

2. Add the app to installed apps

    ```
        INSTALLED_APPS = [
            ...,
            'hurumap'
        ]
    ```
3. Add these to your `settings.py`
    ```

    ```

4. Run migrations
    ```
        python manage.py migrate
    ```
5. Create an admin user to access the CMS
    ```python
       python manage.py createsuperuser
    ```
 

6. Read the [full Wazimap](http://wazimap.readthedocs.org/en/latest/) documentation to get started.

---

## Contributing

To ease contribution, our key principles are borrowed from (contrib)[https://github.com/contrib/contrib] where multiple programming languages and approaches can live together in harmony.

To this end, we've created a [contrib](./contrib) folder that contains the following:
1. [**Docker**](https://docs.docker.com/) scripts for the Django apps powering majority of the backend
2. [**Yarn**](https://yarnpkg.com/en/) implementation for the frontend pieces (coming soon?)
3. [**Makefile**](./Makefile) in the root directory to tie it all together with easy tasks

For more details on contributing, please check out [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Development

### Django Apps

Quickly get started with HURUmap by running the following:

```shell
# 1. Build services:
make build

# 2. Start web server:
make web

# 3. In a new terminal window, load data:
make loaddata
```

Visit http://localhost:8000 to view website.

#### HURUmap Dashboard

HURUmap comes packaged with built-in CMS using Wagtail. To work with the dashboard:

```shell
# 1. Target and build docker image
export DOCKERFILE_TARGET="hurumap-dashboard"
make build

# 2. Start web server:
make web

# 3. In a new terminal window, create your first user:
make createsuperuser
```

Visit http://localhost:8000/dashboard to log into the dashboard.

To remove dashboard workings, stop all services and run;
```shell
unset DOCKERFILE_TARGET
make build
make web
``` 
*NOTE: Unless you remove the database container, all the database tables and their data will remain intact.*

### Frontend UI (Coming Soon)

TODO


### Adding Data

TODO

## Deployment

### Django Apps

TODO

### Frontend UI (Coming Soon)

TODO

---

## License

GNU GPLv3

Copyright (C) 2018  Code for Africa

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
