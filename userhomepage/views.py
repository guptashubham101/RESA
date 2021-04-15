from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
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
        print(request.data)
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return render(request, 'write_recipe/write_recipe.html')


    
def user_homepage(request):
    return render(request, "userhomepage/userhomepage.html")
>>>>>>> e9cd2ae9a791549aa6a7271e806e4e3959155a06
