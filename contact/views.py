from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import QuoteForm

def contact(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            messages.success(request, f'Your request for a quote has been sent!')
            return redirect('/')  # Redirect to a success page or any other desired page
    else:
        form = QuoteForm()

    return render(request, 'contact/contact.html', {'form': form})
