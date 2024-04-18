from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'is_detail_page': False,
    })


def recipe(request, id):
    #  recipes = Recipe.objects.filter(id=id, is_published=True).first()
    recipes = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipes,
        'is_detail_page': True,
    })
