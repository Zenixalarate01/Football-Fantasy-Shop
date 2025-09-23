from django.urls import path
from main.views import show_main, create_item, show_items, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('item/<str:id>/', show_items, name='show_items'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]