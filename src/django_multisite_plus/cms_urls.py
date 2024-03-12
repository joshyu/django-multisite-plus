from django.urls import include

from djangocms_multisite.urlresolvers import cms_multisite_url


urlpatterns = [
    cms_multisite_url(r"^", include("cms.urls")),
]
