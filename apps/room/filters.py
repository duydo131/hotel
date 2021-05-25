import django_filters
import datetime
from django.db.models import Q


class RoomFilterSet(django_filters.FilterSet):
    hotel = django_filters.CharFilter(lookup_expr="exact", field_name="hotel_id")
    day = django_filters.CharFilter(method="start_end_date")

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.distinct()

    def start_end_date(self, queryset, name, value):
        day = value.split(u',')
        if len(day) != 2:
            return queryset

        format = '%Y-%m-%d'
        print(day[0], day[1])
        try:
            d1 = datetime.datetime.strptime(day[0], format)
            d2 = datetime.datetime.strptime(day[1], format)
            if d1 >= d2:
                raise Exception("Date Error")
        except ValueError:
            raise Exception("This is the incorrect date string format. It should be YYYY-MM-DD")

        query = Q(details__rent__start_date__gte=day[1]) | Q(details__rent__end_date__lte=day[0]) | \
                Q(details__rent__end_date__isnull=True)
        return queryset.filter(query)


class RoomCategoryFilterSet(django_filters.FilterSet):
    pass


class ServiceFilterSet(django_filters.FilterSet):
    room = django_filters.CharFilter(lookup_expr="exact", field_name="room_categorys__rooms__id")


class DeviceFilterSet(django_filters.FilterSet):
    pass


class RoomDeviceFilterSet(django_filters.FilterSet):
    room = django_filters.CharFilter(lookup_expr="exact", field_name="room__id")

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.distinct()


class RoomServiceFilterSet(django_filters.FilterSet):
    pass
