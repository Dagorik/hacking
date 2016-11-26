from django.conf.urls import url, include

urlpatterns = [
    url(r'^baston/', include("baston.urls_api_v2")),
]
