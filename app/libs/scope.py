class Scope:
    allow_api = []
    allow_module = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # 去重
        self.allow_api = list(set(self.allow_api))
        return self


class UserScope(Scope):
    # allow_api = ['v1.get_user']
    allow_module = ['v1.user']


class AdminScope(Scope):
    allow_api = []


class SuperScope(Scope):
    # allow_api = ['v1.super_delete_user']

    def __init__(self):
        self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
    # 这里的scope是一个字符串
    scope = globals()[scope]()
    # 添加module，定义endpoint形式为 v1.module_name + view_func，把v1.module_name当作一部分

    splits = endpoint.split('+')
    module_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    if module_name in scope.allow_module:
        return True
    else:
        return False
