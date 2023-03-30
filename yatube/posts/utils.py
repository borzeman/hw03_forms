from django.core.paginator import Paginator


NUM_ART = 10  # Количество выводимых статей


def optimization(post_list, request):  # DRY
    paginator = Paginator(post_list, NUM_ART)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
