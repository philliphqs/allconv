import urllib.request

from resources.variables import *


def download():
    urllib.request.urlretrieve(File.Images.Icon[2], File.Images.Icon[0])
