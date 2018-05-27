from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def buildfullurl(context, page):
    """
    Outputs a page's URL as relative (/foo/bar/) if it's within the same site as the
    current page, or absolute (http://example.com/foo/bar/) if not.
    """
    try:
        current_site = context['request'].site
    except (KeyError, AttributeError):
        # request.site not available in the current context; fall back on page.url
        return page.url

    # Pass page.relative_url the request object, which may contain a cached copy of
    # Site.get_site_root_paths()
    # This avoids page.relative_url having to make a database/cache fetch for this list
    # each time it's called.
    url = page.relative_url(current_site, request=context.get('request'))
    return context.request.build_absolute_uri(url)
