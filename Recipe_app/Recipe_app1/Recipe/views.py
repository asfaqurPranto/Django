from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe
from django.shortcuts import redirect , get_object_or_404
from django.template.context_processors import csrf

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
  recipes = Recipe.objects.all().values()
  context={'recipes':recipes}
  template = loader.get_template('first.html')
  return HttpResponse(template.render(context,request))

# def add_recipe(request):
#     template=loader.get_template('add_recipe_form.html')
#     return HttpResponse(template.render())

def view_base(request):
    template=loader.get_template('base.html')
    return HttpResponse(template.render())

def add_recipe(request):

    # it will be executed when the form is submitted
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        # Basic validation
        if not title or not ingredients or not instructions:
            return HttpResponse("All fields are required.", status=400)

        recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions)
        recipe.save()

        # Redirect to the list of recipes or another view
        return redirect('/Recipe/')  

    return render(request, 'add_recipe_form.html')

# def search(request):
#     if request.method == 'POST':
#         search = request.POST.get('query')
#         recipes = Recipe.objects.filter(title__icontains=search)
#         context = {'recipes': recipes}
#         return render(request, 'first.html', context)
#     return render(request, 'first.html')

def search(request):
    query = request.GET.get('query', '')  # Use GET instead of POST
    recipes = Recipe.objects.filter(title__icontains=query) if query else Recipe.objects.all()
    
    context = {'recipes': recipes, 'query': query}  # Pass query back to template
    return render(request, 'first.html', context)

def Delete(request, recipe):
    recipe_instance = get_object_or_404(Recipe, title=recipe)
    recipe_instance.delete()
    return redirect('/Recipe/') 