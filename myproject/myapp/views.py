# myapp/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q  # Импортируем Q для сложных запросов
from .models import Property


def property_list(request):
    # Получаем базовый набор всех объектов
    queryset = Property.objects.all()

    # --- Фильтрация ---
    search_query = request.GET.get('q', '')
    region_filter = request.GET.get('region', '')
    status_filter = request.GET.get('status', '')
    district_filter = request.GET.get('district', '')

    if search_query:
        # Ищем по нескольким полям: названию, адресу, району
        queryset = queryset.filter(
            Q(name__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(district__icontains=search_query) |
            Q(district__icontains=search_query)
        )

    if region_filter:
        queryset = queryset.filter(region=region_filter)

    if status_filter:
        queryset = queryset.filter(status=status_filter)

    if district_filter:
        queryset = queryset.filter(district=district_filter)

    # --- Количество объектов на странице ---
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in [10, 25, 50]:
        per_page = 10

    # --- Пагинация ---
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Получаем уникальные регионы и статусы для выпадающих списков в фильтре
    regions = Property.objects.values_list('region', flat=True).distinct()
    statuses = Property.objects.values_list('status', flat=True).distinct()
    districts = Property.objects.values_list('district', flat=True).distinct().order_by('district')

    context = {
        'page_obj': page_obj,
        'per_page': per_page,
        'search_query': search_query,
        'region_filter': region_filter,
        'status_filter': status_filter,
        'district_filter': district_filter,
        'regions': regions,
        'statuses': statuses,
        'districts': districts,
    }
    return render(request, 'myapp/property_list.html', context)