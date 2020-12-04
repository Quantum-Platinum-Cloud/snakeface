__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2020, Vanessa SOchat"
__license__ = "MPL 2.0"

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from snakeface.apps.base import urls as base_urls
from snakeface.apps.main import urls as main_urls
from snakeface.apps.users import urls as user_urls

admin.autodiscover()

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(base_urls, namespace="base")),
    url(r"^", include(main_urls, namespace="main")),
    url(r"^", include(user_urls, namespace="users")),
    url(
        r"^robots\.txt?/$",
        TemplateView.as_view(
            template_name="base/robots.txt", content_type="text/plain"
        ),
    ),
]
