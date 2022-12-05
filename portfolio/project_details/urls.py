from django.urls import path
from . import views
# from portfolio.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-project_detail'),
    # path('update/<int:project_detail_id>', views.update_project_detail),
    # path('delete/<int:project_detail_id>', views.delete_project_detail)
]

#DataFlair
# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
