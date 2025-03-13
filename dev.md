# Project Documentation: Django Notes Application

## Project Overview

This application is a Django-based note-taking system that allows users to create, view, and manage notes. The project follows Django's MVT (Model-View-Template) architecture with the following structure:

- **Core**: The main Django project configuration
- **Home**: A basic app with a homepage
- **Notes**: App for handling note creation, listing, and detailed views

## Project Structure

```
project/
├── core/                   # Main Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL routing
│   ├── asgi.py             # ASGI configuration
│   └── wsgi.py             # WSGI configuration
├── home/                   # Home app
│   ├── views.py            # Home view logic
│   ├── urls.py             # Home URL patterns
│   └── models.py           # Empty - no models used
├── notes/                  # Notes app
│   ├── models.py           # Notes data models
│   ├── views.py            # Views for note listing and details
│   ├── urls.py             # Notes URL routing
│   └── admin.py            # Admin configuration for Notes
├── templates/              # HTML templates
│   ├── home/               # Home app templates
│   │   ├── base.html       # Base template with Bootstrap
│   │   └── home.html       # Homepage template
│   └── notes/              # Notes app templates
│       ├── notes_list.html # Template for listing notes
│       └── note_detail.html # Template for note details
├── .gitignore              # Git ignore configuration
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── config.json             # Project configuration (gitignored)
```

## Configuration

The project uses a `config.json` file for configuration, which is excluded from version control. An example structure is provided in `example.json`:

```json
{
    "DEBUG": true,
    "SECRET_KEY": "d#^h846$+=j6s8&7%=vr_*algnus3ye%*pwaa@o#2%i1ls#2$m",
    "ALLOWED_HOSTS": ["localhost","127.0.0.1"],
    "DATABASE": "dev",
    "DB_ENGINE":"",
    "DB_NAME": "",
    "DB_PASSWORD": "",
    "DB_USER":"",
    "DB_PORT":""
}
```

For production, you should:
1. Create a proper `config.json` file
2. Set `DEBUG` to `false`
3. Generate a new `SECRET_KEY`
4. Configure database settings if using a production database

## Models

### Notes Model (`notes/models.py`)

```python
class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]  # Newest notes first
```

The Notes model includes:
- Basic note data (title, content)
- Timestamps for creation and updates
- Likes counter
- Soft delete functionality with `is_deleted` flag

## Views

The project uses a mix of Class-Based Views (CBVs) for most functionality:

### Home View (`home/views.py`)

```python
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = format(timezone.now(), 'Y-m-d H:i:s')
        return context
```

This view displays the homepage and passes the current date to the template.

### Notes Views (`notes/views.py`)

```python
class NotesListView(ListView):
    model = Notes
    template_name = "notes/notes_list.html"
    context_object_name = "notes"
    queryset = Notes.objects.filter(is_deleted=False).order_by("-created_at")

class DetailNoteView(DetailView):
    model = Notes
    template_name = "notes/note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        return Notes.objects.filter(is_deleted=False).order_by("-created_at")

class PopularNotesListView(ListView):
    model = Notes
    template_name = None
    context_object_name = "popular_notes"

    def get_queryset(self):
        return Notes.objects.filter(is_deleted=False, likes__gte=1).order_by("-created_at")
```

These views:
- List all non-deleted notes (`NotesListView`)
- Show detailed view of a specific note (`DetailNoteView`)
- List popular notes (notes with at least one like) - `PopularNotesListView` (Note: this view has no template set and is not used in the current URL configuration)

## URL Routing

### Main URLs (`core/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path('smart/', include('notes.urls')),
]
```

### Home URLs (`home/urls.py`)

```python
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]
```

### Notes URLs (`notes/urls.py`)

```python
urlpatterns = [
    path('notes-list/', views.NotesListView.as_view(), name='notes_list'),
    path('note-detail/<int:pk>/', views.DetailNoteView.as_view(), name='note_detail'),
]
```

## Templates

The project uses Bootstrap 4 for styling with the following template structure:

1. **Base Template** (`templates/home/base.html`): Contains the basic HTML structure, Bootstrap CSS/JS imports, and defines blocks for title and content.

2. **Home Template** (`templates/home/home.html`): Extends the base template to display a welcome message, current date, and link to notes.

3. **Notes List Template** (`templates/notes/notes_list.html`): Shows a table of all notes with title, content preview, likes, and a view button.

4. **Note Detail Template** (`templates/notes/note_detail.html`): Displays the complete details of a single note.

## Admin Configuration

The admin interface is configured to display Notes with relevant information:

```python
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_deleted', 'created_at', 'updated_at', 'likes')

admin.site.register(models.Notes, NotesAdmin)
```

## Installation and Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `config.json` file (use `example.json` as a template)
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`

## Further Development [Under-Progress]

### Missing Features and Improvement Opportunities

1. **User Authentication**: Currently no user authentication system is implemented. Notes are not associated with specific users.

2. **CRUD Operations**: Only view operations are implemented. Need to add:
   - Create note functionality
   - Update note functionality
   - Delete note functionality (currently uses soft delete in admin only)

3. **Likes Functionality**: The model has a likes field, but no interface to increment likes.

4. **Popular Notes View**: The `PopularNotesListView` is defined but not used in URLs.

5. **Root URL**: There's no view associated with the root URL `/`.

6. **Testing**: Limited test files are present but contain no actual tests.

7. **Frontend Enhancement**: The UI is functional but basic.

## Django View Types Reference

### Class-Based Views (CBVs)

```python
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ViewTemplate(LoginRequiredMixin, TemplateView):
    template_name = "test/test.html"
    extra_context = {"context": context}
```

URL configuration:
```python
path('viewTemplate/', views.ViewTemplate.as_view(), name='ViewTemplate')
```

### Function-Based Views (FBVs)

```python
def view(request):
    # data for the database...
    context = {"data": data}
    return render(request, "test/test.html", context)
```

URL configuration:
```python
path('view/', views.view, name='view')
```


```markdown
## Frontend Implementation

### Base HTML Layout

The project uses a standard Bootstrap 4 layout with a container structure that provides consistent styling across all pages:

```html
<!-- templates/home/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" />
        <title>{% block title %}{% endblock title %} |</title>
    </head>
    <body class="container my-3 p-4">
        {% block content %}{% endblock content %}
        <!-- Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </body>
</html>
```

### Template Inheritance

All templates extend the base template to maintain consistent styling and structure. For example:

```html
<!-- templates/notes/notes_list.html -->
{% extends "home/base.html" %}

{% block title %}Notes{% endblock title %}

{% block content %}
    <h1 class="display-4">Notes</h1>
    <!-- Content here -->
{% endblock content %}
```

## Django Template Language Features Used

The project demonstrates several Django Template Language (DTL) features:

1. **Template inheritance**: Using `{% extends %}` and `{% block %}` tags
2. **URL resolution**: With `{% url %}` tags for linking between pages
3. **Conditionals and loops**: Using `{% for %}` and `{% empty %}` tags
4. **Filters**: Such as `{{ note.content | truncatechars:10 }}` to limit content preview length
5. **Comments**: Using `{% comment %}` tags for developer notes

## Database Configuration

The project supports both development (SQLite) and production database configurations:

```python
# core/settings.py
if CONFIG["DATABASE"] == "pro":
    DATABASES = {
        "default": {
            "ENGINE": CONFIG["DB_ENGINE"],
            "NAME": CONFIG["DB_NAME"],
            "USER": CONFIG["DB_USER"],
            "PASSWORD": CONFIG["DB_PASSWORD"],
            "HOST": CONFIG["DB_HOST"],
            "PORT": CONFIG["DB_PORT"],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
```

## Static File Management

The project is configured to handle static files with the following settings:

```python
# core/settings.py
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
<!-- 
## Implementing New Features

### Adding Note Creation Functionality

To implement note creation, you would need:

1. Create a new form class:
```python
# notes/forms.py
from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
```

2. Add a create view:
```python
# notes/views.py
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import NoteForm

class CreateNoteView(CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes_list')
```

3. Update URLs:
```python
# notes/urls.py
path('note-create/', views.CreateNoteView.as_view(), name='note_create'),
```

4. Create a template for the form:
```html


{% extends "home/base.html" %}

{% block title %}Create Note{% endblock %}

{% block content %}
<h1>Create New Note</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Save</button>
</form>
{% endblock %}
```

### Adding Like Functionality

To implement the like functionality:

1. Add a view function:
```python
# notes/views.py
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

def like_note(request, pk):
    note = get_object_or_404(Notes, pk=pk, is_deleted=False)
    note.likes += 1
    note.save()
    return redirect(reverse('note_detail', kwargs={'pk': pk}))
```

2. Update URLs:
```python
# notes/urls.py
path('note-like/<int:pk>/', views.like_note, name='note_like'),
```

3. Add a like button to the detail template:
```html


<form action="{% url 'note_like' pk=note.pk %}" method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-success">Like</button>
</form>
```



## Testing Strategy

While the project currently lacks tests, a proper testing strategy would include:

1. **Model Tests**: Verify model methods and database constraints
2. **View Tests**: Ensure views return correct data and status codes
3. **Form Tests**: Validate form behavior and validation logic
4. **URL Tests**: Confirm URL patterns resolve to correct views
5. **Template Tests**: Check template rendering and context variables

Example model test:
```python
# notes/tests.py
from django.test import TestCase
from .models import Notes

class NotesModelTest(TestCase):
    def setUp(self):
        Notes.objects.create(title="Test Note", content="Test Content")
    
    def test_notes_creation(self):
        note = Notes.objects.get(title="Test Note")
        self.assertEqual(note.content, "Test Content")
        self.assertEqual(note.likes, 0)
        self.assertFalse(note.is_deleted)
```

## Deployment Considerations

For deploying to Ubuntu in production:

1. **WSGI Server**: Configure Gunicorn or uWSGI as a WSGI server
2. **Web Server**: Set up Nginx as a reverse proxy
3. **Database**: Configure PostgreSQL for production use
4. **Static Files**: Set up static file serving with collectstatic
5. **Environment Variables**: Use environment variables for sensitive configuration
6. **SSL/TLS**: Configure HTTPS with Let's Encrypt
7. **Monitoring**: Set up monitoring tools for application health

## Performance Optimization

Future optimizations could include:

1. **Query Optimization**: Monitor and optimize database queries
2. **Caching**: Implement Redis or Memcached for caching
3. **Pagination**: Add pagination to list views for large datasets
4. **Database Indexes**: Add indexes to frequently queried fields
5. **Template Fragment Caching**: Cache parts of templates that don't change often

## Security Considerations

The project has some security practices in place but could benefit from:

1. Ensuring `DEBUG = False` in production
2. Configuring proper `ALLOWED_HOSTS`
3. Implementing proper user authentication and authorization
4. Setting up rate limiting for sensitive views
5. Regular dependency updates
6. Security headers configuration
-->