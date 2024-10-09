from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, confirm_delete_product, delete_product, create_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', confirm_delete_product, name='confirm_delete_product'),  # Confirmation route
    path('delete-product/execute/<uuid:id>/', delete_product, name='delete_product'),  # Actual deletion
    path('create-ajax/', create_product_ajax, name='create_product_ajax'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
