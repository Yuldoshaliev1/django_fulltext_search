from django.urls import path

from .views import QuoteList, SearchResultsList, MainPage

urlpatterns = [
    path("", QuoteList.as_view(), name="all_quotes"),
    path('main', MainPage.as_view(), name='main'),
    path("search/", SearchResultsList.as_view(), name="search_results"),
]