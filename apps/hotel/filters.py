import django_filters
import datetime
from django.db.models import Q

from apps.hotel.models import Hotel


class HotelFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", field_name="name")
    address = django_filters.CharFilter(lookup_expr="icontains", field_name="address")
    adult = django_filters.CharFilter(lookup_expr="gte"
                                      , field_name="rooms__adult")
    children = django_filters.CharFilter(lookup_expr="gte"
                                      , field_name="rooms__children")
    day = django_filters.DateFromToRangeFilter(method="start_end_date")
    price = django_filters.RangeFilter(method="price_range")
    star = django_filters.CharFilter(method="star_choice")

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.distinct()

    def start_end_date(self, queryset, name, value):
        d2 = value.start
        d1 = value.stop
        if d1 >= d2:
            raise Exception("Date Error")

        query = Q(rooms__details__rent__start_date__gte=d1) | Q(rooms__details__rent__end_date__lte=d2) | \
                Q(rooms__details__rent__end_date__isnull=True)
        return queryset.filter(query)

    def price_range(self, queryset, name, value):
        d2 = value.start
        d1 = value.stop
        query = Q()
        if d1 and d2 and d1 < d2:
            raise Exception("Price Error")

        if d1:
            query &= Q(rooms__price__lte=d1)

        if d2:
            query &= Q(rooms__price__gte=d2)

        return queryset.filter(query)

    def star_choice(self, queryset, name, value):
        query = Q()
        try:
            stars = [int(s) for s in value.split(',')]

            for star in stars:
                if star > 5 or star < 1:
                    raise Exception("Rating Error")
                query |= Q(stars=star)
        except Exception:
            raise Exception("Rating Error")
        print(query)
        return queryset.filter(query)

    class Meta:
        models = Hotel
        exclude = ["start", "end"]


class RatingFilterSet(django_filters.FilterSet):
    hotel = django_filters.CharFilter(field_name="hotel__id")
