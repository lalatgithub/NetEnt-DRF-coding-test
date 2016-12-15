"""
app URL Configuration
"""

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^add_genre/$', GenreCreateView.as_view(), name='add-genre'),
    url(r'^add_book/$', BookCreateView.as_view(), name='add-book'),
    url(r'^update_book/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='update-book'),
]
