from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginate(records, request, items=10):
    page = request.GET.get('page', '1')
    paginator = Paginator(records, items)
 
    try:
        page = int(page)
    except ValueError:
        page = 1
 
    try:
        records = paginator.page(page)
    except (EmptyPage, InvalidPage):
        records = paginator.page(paginator.num_pages)
    return records

