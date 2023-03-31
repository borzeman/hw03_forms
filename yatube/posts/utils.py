from django.core.paginator import Paginator


def get_page_paginator(post_list, request, NUM_ART):
    paginator = Paginator(post_list, NUM_ART)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
