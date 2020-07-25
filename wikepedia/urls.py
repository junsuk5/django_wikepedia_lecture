"""wikepedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from urllib.request import urlopen

from bs4 import BeautifulSoup
from django.conf.urls import url
# Serializers define the API representation.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request):
        html = urlopen("https://ru.wiktionary.org/wiki/%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C%D1%81%D1%8F")
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find("table", {"class": "morfotable ru"})

        return Response({'html': result.prettify()})


# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^test', TestView.as_view()),
]
