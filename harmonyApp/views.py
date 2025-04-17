from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ContactForm

def index_view(request):
    # Render index.html and pass an instance of ContactForm
    form = ContactForm()
    return render(request, 'harmonyApp/index.html', {'form': form})

def SOX_requirements_view(request):
    form = ContactForm()
    return render(request, 'harmonyApp/SOX_requirements.html', {'form': form})

def Inserting_terminals_into_organization_view(request):
    form = ContactForm()
    return render(request, 'harmonyApp/Inserting_terminals_into_organization.html', {'form': form})

def Purchase_Order_Tracking_view(request):
    form = ContactForm()
    return render(request, 'harmonyApp/Purchase_Order_Tracking.html', {'form': form})

def priority_shortcuts_view(request):
    form = ContactForm()
    return render(request, 'harmonyApp/priority_shortcuts.html', {'form': form})

def priority_view(request):
    # Render index.html and pass an instance of ContactForm
    form = ContactForm()
    return render(request, 'harmonyApp/priority.html', {'form': form})

def contact_view(request):
    # Determine the next URL from the GET or POST parameters, default to 'index'
    next_url = request.GET.get('next') or request.POST.get('next') or 'home'
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            # Save the contact submission to the database
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            # Redirect to the next URL, which may be 'index' or 'about' or any other page
            return redirect(next_url)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            # For non-AJAX requests, fall through to re-render the form with errors
    
    # Render the contact template, also passing the next_url so it can be added as a hidden field if needed.
    return render(request, 'harmonyApp/contact.html', {'form': form, 'next': next_url})


def about_view(request):
    # Render about.html and pass an instance of ContactForm
    form = ContactForm() 
    return render(request, 'harmonyApp/about.html', {'form': form})

def recommendation_view(request):
    form = ContactForm() 
    return render(request, 'harmonyApp/recommendation.html', {'form': form})
    