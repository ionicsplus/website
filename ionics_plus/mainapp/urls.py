from django.urls import path
from .views import main_app,user_signup_page,user_page,log_in_page,log_out_page,query_done_page,adding_request_page,request_sent_page,control_page,edit_page,update_page,payment_page


urlpatterns = [

    path('',main_app,name = 'mainapp'),
    path('signup/',user_signup_page,name = 'signup'),
    path('login/',log_in_page,name ='login'),
    path('logout/',log_out_page,name ='logout'),
    path('user/',user_page,name = 'userpage'),
    path('query/',query_done_page,name = 'querydonepage'),
    path('addrequest/',adding_request_page,name = 'addrequestpage'),
    path('requestsent/',request_sent_page,name = 'requestsent'),
    path('control/',control_page,name = 'controlpage'),
    path('edit/<int:id>',edit_page),
    path('update/<int:id>',update_page),

    path('payment/<int:id>',payment_page,name = 'paymentpage'),


    



    

]