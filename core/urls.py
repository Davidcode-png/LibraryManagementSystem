from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (home,sign_in,sign_up,test,view_books,
                    view_issued_books,add_to_issue,delete_issued_book,
                    sign_out,about)
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls,name='admin'),
    path('',home,name='home'),
    path('login/',sign_in,name='sign_in'),
    path('register',sign_up,name='sign_up'),
    path('test/',test,name='test'),
    path('view/',view_books,name='view_book'),
    path('view_issued/',view_issued_books,name='view_issued'),
    path('about/',about,name='about'),
    path('add_to_issue/<int:pk>',add_to_issue,name='add_to_issue'),
    path('delete_to_issue/<int:pk>',delete_issued_book,name='delete_to_issue'),
    path('logout/',sign_out,name='sign_out'),

]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)