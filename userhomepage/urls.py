from django.urls  import path
from . import views
#from django.conf.urls import reverse
urlpatterns =[ 

path('userhomepage/', views.userhomepage, name  ='userhomepage'),
path('write_recipe/', WriteRecipeApiView.as_view(), name  ='writeRecipe'),
path('', WriteRecipeApiView.as_view(), name  ='postRecipe'),

]