from ..models import RequestLog

class RequestLogMidleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        scheme = request.scheme
        method = request.method
        path = request.path
        status = response.reason_phrase
        code = response.status_code

        request_data = RequestLog(
            scheme=scheme,
            method=method,
            path=path,
            status=status,
            code=code,
        )

        request_data.save()


        # Code to be executed for each request/response after
        # the view is called.

        return response