from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from register.models import *
from recipe_scrapers import scrape_me

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
        print()


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

class UploadLinkApiView(APIView):
    # 1. List all
    def post(self, request, *args, **kwargs):
        inputurl = request.data["urlink"]
        
        scraper = scrape_me(inputurl)
        ingredients_required= scraper.ingredients()
        recipe = ExtractedRecipe.objects.create(
                    userId = request.user,
                    recipe_template = scraper.instructions(),
                    recipe_title = scraper.title()
                )
        for x in ingredients_required:
            Ingredients.objects.create(
                    recipeId = recipe,
                    ingredient_name = x
            )
 

        # Ingredients.objects.create(
        #             recipeId = recipe,
        #             ingredient_name = request.data["feedurl[]"]
        #         )
        return render(request, 'upload_link/upload_link.html')
    def get(self, request, *args, **kwargs):
        
        #return render(request, 'write_recipe/write_recipe.html')
        return render(request, 'upload_link/upload_link.html')
    
def user_homepage(request):
    # 1. List all
    print('calling',request.GET.get('searchbox'))

    if request.GET.get('searchbox') is None:
        print(request.user)
        queryset = ExtractedRecipe.objects.filter(userId=request.user)
        #sorting by name
        queryset = queryset.order_by("recipe_title")
    else:
        print('search was called' , request)
        queryset = None
        key = request.GET.get('searchbox')
        if(key == ""):
            queryset = ExtractedRecipe.objects.filter(userId=request.user)
            #sorting by name
            queryset = queryset.order_by("recipe_title")
        else:
            print(str(key))
            print(request.user)
            queryset1 = Ingredients.objects.filter(ingredient_name__icontains=str(key)).values("recipeId")
            t_set = list(queryset1)
            q_set = []
            for i in t_set:
                q_set += [i["recipeId"]]
            queryset1 = ExtractedRecipe.objects.filter(userId=request.user).filter(id__in=q_set)
            queryset = ExtractedRecipe.objects.filter(userId=request.user).filter(recipe_title__icontains=str(key))
            queryset = queryset.union(queryset1)
            queryset = queryset.order_by("recipe_title")
            pass
    return render(request, "userhomepage/userhomepage.html", {'queryset': queryset})

'''def get_Recipe(request):

        print('*********  get_recipe func ***************')

        recipeId=request.GET.get('recipe_id')
        recipe = ExtractedRecipe.objects.get(id=recipeId)
        ingredient=Ingredients.objects.filter(recipeId=recipeId)
        
        return render(request,'write_recipe/recipe.html',{'recipe': recipe, 'ingredients': ingredient})
'''


class GetRecipeView(APIView):

    def get(self, request, *args, **kwargs):

        print('*********  get_recipe func ***************')

        recipeId=request.GET.get('recipe_id')
        print('get recipe id',recipeId)
        recipe = ExtractedRecipe.objects.get(id=recipeId)
        recipeList = recipe.recipe_template.split(".")
        ingredient=Ingredients.objects.filter(recipeId=recipeId)
        ingredientList = []
        ingredientStr = ''
        for i in ingredient:
            ingredientList.append(i.ingredient_name)
            ingredientStr = ingredientStr + i.ingredient_name + '* '
        
        
        return render(request,'write_recipe/recipe.html',{'recipe': recipe,'recipeList': recipeList, 'ingredients': ingredientList,'ingredientStr': ingredientStr})

    def post(self, request, *args, **kwargs):

        print('post write recipe')

        recipeId=request.GET.get('recipe_id')
        recipe = ExtractedRecipe.objects.get(id=recipeId)
        ingredient= Ingredients.objects.filter(recipeId=recipeId).first()

        recipe.recipe_title=request.data['title']
        recipe.recipe_template=request.data['recipe']
        ingredient.ingredient_name = request.data['feedurl[]']
        Ingredients.objects.filter(recipeId=ingredient.recipeId).delete()
        for x in request.data['feedurl[]'].split('* '):
            Ingredients.objects.create(
                    recipeId = ingredient.recipeId,
                    ingredient_name = x
            )

        recipe.save()

        queryset = ExtractedRecipe.objects.filter(userId=request.user)
        print(recipe.recipe_title)
        print(recipe.recipe_template)
        print(ingredient.ingredient_name)

        return render(request, 'userhomepage/userhomepage.html', {'queryset': queryset})
