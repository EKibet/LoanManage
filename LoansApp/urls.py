from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('stepone/', views.create_loan_step1, name='step_one'),
    path('steptwo/', views.create_loan_step2, name='step_two'),
    path('stepthree/', views.create_loan_step3, name='step_three'),
    path('stepfour/', views.create_loan_step4, name='step_four'),
    path('stepfive/', views.create_loan_step5, name='step_five'),
    path('stepsix/', views.create_loan_step6, name='step_six'),
    path('stepseven/', views.create_loan_step7, name='step_seven'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
