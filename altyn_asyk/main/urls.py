from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index_page', views.index_page, name='index_page'),
    path('about', views.about, name='about'),
    path('bsn', views.bsn, name='bsn'),
    path('license', views.license, name='license'),
    path('community', views.community, name='community'),
    path('documents', views.documents, name='documents'),
    path('training', views.training, name='training'),
    path('medicine', views.medicine, name='medicine'),
    path('psychology', views.psychology, name='psychology'),
    path('covid', views.covid, name='covid'),
    path('bulleten', views.bulleten, name='bulleten'),
    path('register', views.register, name='register'),
    path('adaptation', views.adaptation, name='adaptation'),
    path('security', views.security, name='security'),
    path('relationship', views.relationship, name='relationship'),
    path('schedule', views.schedule, name='schedule'),
    path('food_menu', views.food_menu, name='food_menu'),
    path('open_study', views.open_study, name='open_study'),
    path('mornings', views.mornings, name='mornings'),
    path('zhangyru', views.zhangyru, name='zhangyru'),
    path('aula', views.aula, name='aula'),
    path('ish', views.ish, name='ish'),
    path('top', views.top, name='top'),
]