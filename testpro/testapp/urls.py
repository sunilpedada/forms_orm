from django.conf.urls import url
from testapp import views
urlpatterns=[
    url(r"^$",views.home),
    url(r"^add_players/$",views.add),
    url(r"^display_list/$",views.display_list)
]