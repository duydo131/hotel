from django.middleware.cache import UpdateCacheMiddleware

from core.task import update_cache


class RemoveCacheByPathMiddleware(UpdateCacheMiddleware):
    def process_response(self, request, response):
        if response.streaming or response.status_code not in (200, 304, 201):
            return response

        if request.method not in ('GET', 'HEAD'):
            path = request.path
            update_cache.apply_async(args=(path,))

        return response
