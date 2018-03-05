import json
import logging

from api import errors
from django.http import HttpResponse
from django.utils import six

api_log = logging.getLogger('api')


class Api:
    csrf_exempt = True
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    need_authorize = True
    authenticator = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if key in self.http_method_names:
                raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))

        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise errors.MethodError

    def __handler_need_authorize(self, request):
        pass

    def __get_sign(self, request):
        signture = request.META.get('HTTP_BUNNY', None)
        return signture

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def __call__(self, request, *args, **kwargs):
        errno = 0
        errmsg = ''
        data = None

        try:
            if self.need_authorize:
                signture = self.__get_sign(request)
                self.user_id = self.authenticator.sign_to_user_id(signture)
            data = self.dispatch(request, *args, **kwargs)
        except errors.ApiError as error:
            api_log.exception('%s-%s' % (error.errno, error.errmsg))
            errno = error.errno
            errmsg = error.errmsg
        except:
            api_log.exception('服务器异常')
            errno = errors.ApiError.errno
            errmsg = errors.ApiError.errmsg

        result = {
            'errno': errno,
            'errmsg': errmsg,
            'data': data,
        }

        return HttpResponse(json.dumps(result), content_type='application/json')
