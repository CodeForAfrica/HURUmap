# HURUmap
HURUmap is an interactive web platform that allows citizens and journalists to explore, visualise, and download census data. This gives them the power to give context to stories that was otherwise hard to spot. Accessible at https://hurumap.org

HURUmap relies on the excellent Wazimap and Census Reporter projects.

## Usage

1. Install the package

    ```
    pip install -e git+https://github.com/CodeForAfricaLabs/HURUmap.git@develop#egg=hurumap

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

## License

MIT License

Copyright (c) 2018 Code for Africa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
