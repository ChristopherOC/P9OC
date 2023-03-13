from django.shortcuts import render
from .models import FindUser
from django.views import View

# Create your views here.
# class SearchUser(View):
#     def get(self, request):
#         query = request.get('q')
#         users = None
#         if query:
#             users = FindUser.search(query)
        
#         context = {'query': query, 'users': users}
#         return render(request, 'search_user.html', context)