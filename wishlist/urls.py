from django.urls import path
from wishlist.views import show_json
from wishlist.views import show_xml
from wishlist.views import show_wishlist
from wishlist.views import show_json_by_id
from wishlist.views import register #Import fungsi register dari views
from wishlist.views import login_user # Import fungsi login user
from wishlist.views import logout_user # Import fungsi logout user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='http_response'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), #Path untuk login ke fungsi register yang dibuat dalam views
    path('login/', login_user, name='login'), # Path untuk fungsi login user
    path('logout/', logout_user, name='logout'), # Path untuk fungsi logout user
]