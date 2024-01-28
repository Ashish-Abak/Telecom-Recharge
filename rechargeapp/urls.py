from django.contrib import admin
from django.urls import path
from rechargeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login',views.login_user),
    path('logout',views.logout_user),
    path('register',views.register),
    path('planfilter/<dt>/Day',views.planfilter),
    path('pdetails/<pid>',views.pdetails),
    path('sort/<pr>',views.sort),
    path('sorts/<pr>',views.sorts),
    path('payment/<pid>',views.payment),
    path('sendmail',views.sendmail),
    path('prepaid',views.prepaid),
    path('postpaid',views.postpaid),
    path('true5g',views.true5g),
    path('locate',views.locate),
    path('contact',views.contact),
    path('about',views.about),
]
