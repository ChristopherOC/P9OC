from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ReviewForm, TicketForm
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
    
class CreateTicket(View):
    form_class = TicketForm
    template_name = 'create_ticket.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            print(ticket.user)
            reverse('feed', kwargs={'form': form, 'ticket': ticket})
        return redirect('feed')
#rechercher dans le cours la gestion des idea foreigney etc...
