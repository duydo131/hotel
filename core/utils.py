import pytz
from rest_framework import serializers

timezone = pytz.timezone('Asia/Ho_Chi_Minh')

from django.db import connection, reset_queries
import time
import functools

def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print("Function : " + func.__name__)
        print("Number of Queries : {}".format(end_queries - start_queries))
        print("Finished in : {}".format(end - start))

        return result

    return inner_func


def localize_datetime(datetime):
    return timezone.localize(datetime)


def create_model(data, Serializer):
    try:
        serializer = Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
    except Exception as e:
        raise Exception
