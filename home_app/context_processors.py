# home_app/context_processors.py
from Daroos_app.models import Category

def categories_context(request):
    categories = Category.objects.all()
    return {'sidebar_categories': categories}
