from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginate(records, request, items=10):
    """
    make paginate easy... :
    
    from common.utils import paginate
    objects = MyModel.objects.all()
    # paginate all the objects 5 items per pages
    objects_paginated = paginate(objects, request, 5)
    
    
    objects_paginated can now be used in your template
    - objects_paginated.has_next (boolean if has next record)
    - objects_paginated.has_previous (boolean if has previous record)
    - objects_paginated.object_list (return objects)
    - objects_paginated.page (actual page)...

    To manage pages in your template:
    {% if objects.has_next %}
        <a href="?page={{ objects.next_page_number }}">next</a>
    {% endif %}
    {% if objects.has_previous %}
        <a href="?page={{ objects.previous_page_number }}">previous</a>
    {% endif %}
    """
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

