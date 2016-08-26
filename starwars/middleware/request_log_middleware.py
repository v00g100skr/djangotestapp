from ..models import RequestLog

class RequestLogMidleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

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

        return response