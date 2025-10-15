from django.urls import path
from main.views import show_main, create_item, show_items, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_item, delete_item, add_item_ajax, login_ajax, register_ajax, update_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('item/<str:id>/', show_items, name='show_items'),
    path('item/<str:id>/edit/', edit_item, name='edit_item'),
    path('item/<str:id>/delete/', delete_item, name='delete_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('update-item-ajax/<str:id>/', update_item_ajax, name='update_item_ajax'),
]