from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    ingredient_count = int(request.GET.get("servings", 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * ingredient_count,
            'молоко, л': 0.1 * ingredient_count,
            'соль, ч.л.': 0.5 * ingredient_count,
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    ingredient_count = int(request.GET.get("servings", 1))
    context = {
        'pasta': {
            'макароны, г': 0.3 * ingredient_count,
            'сыр, г': 0.05 * ingredient_count,
        },
    }
    return render(request, 'calculator/index2.html', context)


def buter(request):
    ingredient_count = int(request.GET.get("servings", 1))
    context = {
        'buter': {
            'хлеб, ломтик': 1 * ingredient_count,
            'колбаса, ломтик': 1 * ingredient_count,
            'сыр, ломтик': 1 * ingredient_count,
            'помидор, ломтик': 1 * ingredient_count,
        },
    }
    return render(request, 'calculator/index3.html', context)