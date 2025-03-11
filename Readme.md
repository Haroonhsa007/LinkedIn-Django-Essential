# LinkedIn-Django-Essential #


##  Class Based Views ##

```py
from django.view.generic import TemplateView

# for auth us mixins

from django.contrib.auth.mixins import LoginRequiredMixin 

# add it before TemplateView

class ViewTemplate(LoginRequiredMixin, TemplateView):
    template_name = "test/test.html"
    extra_context = {"context":context}
```
### class view urls ###

```py
from django.urls import path
from . import views

urlpatterns = [
    path('viewTemplate/', views.ViewTemplate.as_view(), name='ViewTemplate'),
```

## Function Based Views ##

```py
def view(request):
    # data for the database...

    context = {"data": data}

    return render(request, "test/test.html", context)
```

### Function Based Views url ###
```py
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view, name='view'),
]
```