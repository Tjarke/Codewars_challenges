"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"


"""


def domain_name(url):
    www = url.find("www.")
    slsl = url.find("//")
    if www != -1:
        dom = url[www+4:].split(".")[0]
    elif slsl != -1:
        dom = url[slsl+2:].split(".")[0]
    else:
        dom = url.split(".")[0]
    return dom

"""
better:
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
"""