import webbrowser
from urllib.parse import quote_plus


def open_web(target):
    return webbrowser.open(target)


def search_web(target):
    query = quote_plus(target)
    url = f"https://www.google.com/search?q={query}"
    return webbrowser.open(url)


TOOL_REGISTRY = {
    'opening': open_web,
    'searching': search_web
}

