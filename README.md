# HURUmap
HURUmap is an interactive web platform that allows citizens and journalists to explore, visualise, and download census data. This gives them the power to give context to stories that was otherwise hard to spot. Accessible at https://hurumap.org

HURUmap is a fork of the excellent Wazimap/Censusreporter project which was funded by a Knight News Challenge grant. You can also find Censusreporter on GitHub.

## Usage

1. Install the package

    ```
    pip install

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

5. Read the [full Wazimap](http://wazimap.readthedocs.org/en/latest/) documentation to get started.