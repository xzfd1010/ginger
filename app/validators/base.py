from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self, data=None):
        # 这里的data就是需要校验的数据
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()  # 父类validate
        # valid = self.validate() # 只执行自己的

        if not valid:
            raise ParameterException(msg=self.errors)

        return self
