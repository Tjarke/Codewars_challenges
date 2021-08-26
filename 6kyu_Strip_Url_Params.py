"""
Complete the method so that it does the following:

    Removes any duplicate query string parameters from the url (the first occurence should be kept)
    Removes any query string parameters specified within the 2nd argument (optional array)

Examples:

strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
"""


def strip_url_params(url, params_to_strip=None):
    if '?' not in url:
        return url
    if not params_to_strip:
        params_to_strip = []
    list_params = url[url.index('?')+1:].split('&')
    return_url = url[:url.index('?')+1]
    params = []
    for i in list_params:
        current = i.split('=')
        if (current[0] not in params) and (current[0] not in params_to_strip):
            params.append(current[0])
            return_url += i + '&'
    return return_url[:-1]
