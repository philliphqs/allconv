import webbrowser
import platform

from resources.variables import *


def GitHub():
    webbrowser.open(URL.GitHub)


def GitHubReleases():
    webbrowser.open(URL.GitHubReleases)


def GitHubLatestRelease():
    webbrowser.open(URL.GitHubLatestRelease)


def GitHubLatestReleaseDownload():
    webbrowser.open(URL.GitHubLatestReleaseDownload)


def Website():
    webbrowser.open(URL.Website)


def Help():
    webbrowser.open(URL.Help)


def report_bug():
    body = f'body=%23%23%23%23%20Description%0A' \
           f'%23%23%23%23%23%23%20...%0A' \
           f'%23%23%23%23%20Environment%0A' \
           f'%20*%20{Product.Name}%0A' \
           f'%20*%20Platform:%20{platform.system()}%0A' \
           f'%20*%20Arch:%20{platform.architecture()[0]}%0A' \
           f'%20*%20OS%20Version:%20{platform.version()}%0A' \
           f'%20*%20Python%20Version:%20{platform.python_version()}%0A' \
           f'%20*%20Proccesor:%20{platform.processor()}%0A' \
           f'%20*%20App%20Version:%20' + Product.Version
    webbrowser.open(url=f'https://github.com/philliphqs/{Product.Name}/issues/new?title=[Bug]%20&' + body)


def request_a_feature():
    body = f'body=%23%23%23%23%20Description%0A' \
           f'%23%23%23%23%23%23%20Describe%20the%20feature%0A'
    webbrowser.open(url=f'https://github.com/philliphqs/{Product.Name}/issues/new?title=[Feature]%20&' + body)
