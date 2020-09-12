#
# Create a function that takes a URL (string), removes duplicate query parameters and parameters specified within the
# 2nd argument (which will be an optional list).
#
#
# def strip_url_params(url, params_to_strip):
#
#


def strip_url_params(url, exclude=[]):
    if "?" not in url:
        return url
    base, params = url.split("?")
    params = dict(x.split("=") for x in params.split("&"))
    params = [(k, params[k]) for k in sorted(params) if k not in exclude]
    return base + "?" + "&".join("=".join(x) for x in params)
