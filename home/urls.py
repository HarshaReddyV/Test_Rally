from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('profile', views.profile, name='profile'),
    path('watchlist', views.WatchListView, name='watchlist'),
    path('signout', views.signout, name='signout'),
    path('share/<int:id>', views.details, name ='details'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('watch/<int:id>/', views.Watch, name ='watch'),
    path('removewatch/<int:id>/', views.RemoveWatch, name = 'removewatch'),
    path('data', views.data, name='data'),
    path('typeahead/', views.TypeaheadView.as_view(), name='typeahead'),

]