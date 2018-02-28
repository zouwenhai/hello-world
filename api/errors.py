class ApiError(Exception):

    errno = 1314
    errmsg = '程序员相亲去了，得等会'

    def __init__(self, msg=None, *args):
        if msg is not None:
            self.errmsg = msg
        super().__init__(*args)


class MethodError(ApiError):

    errno = 1414
    errmsg = '别瞎JB请求'
