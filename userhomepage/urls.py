from django.urls  import path
from . import views
#from django.conf.urls import reverse
urlpatterns =[ 

path('userhomepage/', views.userhomepage, name  ='userhomepage'),
path('write_recipe/', WriteRecipeApiView.as_view(), name  ='writeRecipe'),
path('', WriteRecipeApiVpath('get_Recipe/', GetRecipeView.as_view(), name='getRecipe'),
    path('', GetRecipeView.as_view(), name  ='updateRecipe'),iew.as_view(), name  ='postRecipe'),
#path('get_recipe/', get_recipe, name='getRecipe'),
path('get_Recipe/', GetRecipeView.as_view(), name='getRecipe'),
path('', GetRecipeView.as_view(), name  ='updateRecipe'),

]