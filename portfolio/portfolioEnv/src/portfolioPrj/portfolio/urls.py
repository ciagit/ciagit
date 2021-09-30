from django.urls import path
from . import views
urlpatterns=[
    path('info/',views.info, name="info"),
    path('',views.homepage),
    path('experience/',views.experience, name="experience"),
    path('education/',views.education, name="education"),
    path('skills/',views.skills, name="skills"),
    path('interest/',views.interest, name="interest"),
    path('awards/',views.awards, name="awards")
    
]