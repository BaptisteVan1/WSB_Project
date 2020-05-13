from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    # ex: /restaurants/
    path('', views.index, name='index'),

    # ex: /restaurants/15
    path('<int:restaurant_id>/', views.details, name='details'),

    # ex: /restaurants/newrestaurant
    path('newrestaurant', views.new_restaurant.as_view(), name='NewRestaurant'),

    # ex: /restaurants/test
    path('<int:restaurant_id>/reviewing', views.Reviewing.as_view(), name='reviewing'),

    path('edit/review/<int:pk>', views.EditReview.as_view(), name='edit-review'),

    # ex: /restaurants/search_results
    path('search/', views.SearchResults.as_view(), name='search_results'),

    path('welcome/', views.welcome, name='welcome'),
]

