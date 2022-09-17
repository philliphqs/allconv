from win10toast import ToastNotifier

from resources.variables import *


def notifiy(title: Product.Name, message):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                       message,
                       icon_path=File.Icons.Icon,
                       duration=5)
