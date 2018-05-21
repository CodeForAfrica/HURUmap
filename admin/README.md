## CMS admin App

Quick start
-----------

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'admin',
    ]
    
2. Add `blog` apps and middleware to `settings.py`
    ```python
    from admin import CMS_ADMIN_APPS, CMS_ADMIN_MIDDLEWARE
    MIDDLEWARE += CMS_ADMIN_MIDDLEWARE
    INSTALLED_APPS += CMS_ADMIN_APPS
    ```

3. Include the polls URLconf in your project urls.py like this::

    ```python
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^blog/', include(blogs_urls)),
    ```

4. Run `python manage.py migrate` to create the `blog` models.