from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home),
    path('',views.login,name="admin"),
   # path('',views.index,name="index"),
   path('page2',views.page2,name="page2"),
   # path('perinfo',views.perinfo,name="perinfo"),
    path('check',views.check,name="check"),
    path('check',views.check,name="check"),
    #path('classify',views.upload_classify,name="upload_classify"),
    #path('segmentation',views.upload_segmentation,name="upload_segmentation"),
    #path('csvmodel',views.upload_csvmodel,name="upload_csvmodel"),
    #path('foldermodel',views.upload_foldermodel,name="upload_foldermodel"),
]