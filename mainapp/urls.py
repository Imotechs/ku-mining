
from django.urls import path,include
from .views import home,news,testimonial,terms,about
urlpatterns = [
    path('', home, name = 'home'),
    path('news/', news, name = 'news'),
    path('our/privacy/policies/', terms, name = 'terms'),
    path('about/us/', about, name = 'about'),
    path('testimonials/',testimonial, name = 'testimonial'),

]
