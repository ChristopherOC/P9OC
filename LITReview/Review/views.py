from django.shortcuts import render, redirect
from django.views import View
from .forms import ReviewForm
from Accounts.models import Ticket


# Create your views here.
class CreateReview(View):
    form_class = ReviewForm
    template_name = 'create_review.html'

    def get(self, request):
        form = self.form_class()
        tickets = Ticket.objects.all()
        return render(request, self.template_name, {'form': form, 'tickets': tickets})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('feed')
        return render(request, self.template_name, {'form': form})
    
#rechercher dans le cours la gestion des idea foreigney etc...
