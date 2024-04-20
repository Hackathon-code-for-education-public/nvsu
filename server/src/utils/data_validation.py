from marshmallow import Schema, fields, validate, ValidationError, validates
from config import UserConfig
import re


class UserRegistrationSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(max=UserConfig.MAX_STRING_LENGTH))
    surname = fields.Str(required=True, validate=validate.Length(max=UserConfig.MAX_STRING_LENGTH))
    father_name = fields.Str(validate=validate.Length(max=UserConfig.MAX_STRING_LENGTH), allow_none=True,
                             missing=None)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=UserConfig.MIN_PASSWORD_LENGTH))

    @validates('password')
    def validate_password(self, value):
        # Проверяем, содержит ли пароль хотя бы одну заглавную букву и один спецсимвол
        if not re.search(r'[A-Z]', value) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValidationError("Пароль должен содержить как минимум один специальный символ и "
                                  "одну букву в верхнем регистре.")
