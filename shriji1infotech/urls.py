from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('about_us/',views.about_us,name='about_us'),
   path('website_development/',views.website_development,name='website_development'),
   path('application_development/',views.application_development,name='application_development'),
   path('e_commerce_solution/',views.e_commerce_solution,name='e_commerce_solution'),
   path('graphic_design/',views.graphic_design,name='graphic_design'),
   path('contact_us/',views.contact_us,name='contact_us'),
   path('php/',views.php,name='php'),
   path('asp/',views.asp,name='asp'),
   path('python/',views.python,name='python'),
   path('java/',views.java,name='java'),
   path('android/',views.android,name='android'),
   path('send_message/',views.send_message,name='send_message'),
]