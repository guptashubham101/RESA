from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from register.models import *
# Create your views here.

class WriteRecipeApiView(APIView):
    # 1. List all
    print('hey')
    def get(self, request, *args, **kwargs):
        print('123')
        return render(request, 'write_recipe/write_recipe.html')

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request)
        print(request.data["title"])
        print(request.data["feedurl[]"])
        print(request.data["recipe"])


        print(request.user)
        print(request.user.first_name)
        recipe = ExtractedRecipe.objects.create(
                    userId = request.user,
                    recipe_template = request.data["recipe"],
                    recipe_title = request.data["title"]
                )

        print(recipe)

        Ingredients.objects.create(
                    recipeId = recipe,
                    ingredient_name = request.data["feedurl[]"]
                )
 
       

        return render(request, 'write_recipe/write_recipe.html')


    
def user_homepage(request):
    return render(request, "userhomepage/userhomepage.html")
