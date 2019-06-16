class SuperScope:
    allow_api = ['v1.super_delete_user']


class UserScope:
    allow_api = []


def is_in_scope(scope, endpoint):
    # 这里的scope是一个字符串
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
