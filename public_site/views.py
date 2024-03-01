from .forms import ContactEntryForm
from .models import ContactSubmission
from .models import Directory
from django.contrib import messages
from datetime import datetime
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.decorators.http import require_POST
import datetime


@require_POST
def submit_form(request):
    # Extract form data
    # ... your form processing logic ...

    # Save the form data
    submission = ContactSubmission(
        forename=request.POST.get('forename'),
        surname=request.POST.get('surname'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone', ''),
        url=request.POST.get('url', ''),
        type_of_contact=request.POST.get('type_of_contact'),
        message=request.POST.get('message'),
        page_id=request.POST.get('page_id', ''),
        filepath=request.POST.get('filepath', ''),
        datetime=timezone.now(),
        ip_address=get_client_ip(request),
        browser_specs=request.POST.get('browser_specs')
    )
    submission.save()

    # Add a success message
    messages.success(request, 'Thank you for your submission!')

    # Redirect to the referring page or a fallback
    referrer = request.META.get('HTTP_REFERER', 'home')
    return redirect(referrer)

def get_client_ip(request):
    """Get the client IP address from the request object."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    # Fetch top-level directories
    top_level_directories = Directory.objects.filter(parent_id__isnull=True)
    return render(request, 'index.html')

    # Serialize all directory data into JSON for search functionality
    directories_json = serialize('json', Directory.objects.all())

    return render(request, 'home.html', {
        'subdirectories': top_level_directories,
        'directories_json': directories_json
    })
        
def directory_main_view(request, directory_id=None):
    if directory_id:
        # Display specific directory and its children
        directory = get_object_or_404(Directory, id=directory_id)
        subdirectories = directory.subdirectories.all()  # Assuming 'subdirectories' is the related name for child directories

        # Set page title to the title of the current directory
        page_title = directory.title  # Use the title of the directory

        # Build breadcrumbs
        breadcrumbs = [{'title': 'Home', 'url': '/'}]  # Start with Home
        current = directory.parent  # Start with the parent of the current directory
        while current is not None:
            breadcrumbs.append({
                'title': current.title,
                'url': '/directory/' + str(current.id)
            })
            current = current.parent  # Move to the parent

        # Append the current directory at the end without a URL
        breadcrumbs.append({'title': directory.title, 'url': None})

        context = {
            'current_directory': directory,
            'subdirectories': subdirectories,
            'page_title': page_title,  # Updated page title
            'breadcrumbs': breadcrumbs  # Add breadcrumbs to context
        }
    else:
        # Display top-level directories
        directory = None
        subdirectories = Directory.objects.filter(parent=None)
        context = {
            'current_directory': directory,
            'subdirectories': subdirectories,
        }
    return render(request, 'directory/directory_main.html', context)


def static_page(request, page):
    # Mapping page names to their breadcrumb titles
    breadcrumb_titles = {
        'test_page': 'Test Page',
        'about_us': 'About Us',
        'contact': 'Contact',
        'sponsorship': 'Sponsorship'
    }

    # Generate breadcrumbs
    breadcrumbs = [
        {'title': 'Home', 'url': '/'},
        {'title': breadcrumb_titles.get(page, page.capitalize()), 'url': '#'}
    ]

    context = {
        'breadcrumbs': breadcrumbs
    }

    template_name = f'pages/{page}.html'
    return render(request, template_name, context)


def current_year(request):
    context = {
        'current_year': datetime.now().year,
        # ... other context data
    }
    return render(request, 'layout/base.html', context)
