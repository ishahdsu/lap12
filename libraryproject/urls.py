from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("Apps.bookmodule.urls")), #include urls.py of bookmodule app
    path('users/', include("Apps.usermodule.urls")) , #include urls.py of usermodule app
    path('user/', include("Apps.usermodule.urls"))  #include urls.py of usermodule app
    
]
