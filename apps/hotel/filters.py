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

    class Meta:
        models = Hotel
        exclude = ["start", "end"]


class RatingFilterSet(django_filters.FilterSet):
    hotel = django_filters.CharFilter(field_name="hotel__id")
