from . import views
from django.conf.urls import url


urlpatterns = [
    url(r"^write", view=views.writeMessage),
    url(r"^read", view=views.readMessage),
    url(r"^delete", view=views.deleteMessage),
    url(r"^getall", view=views.getAll),
    url(r"^getunread", view=views.getUnread)
]
