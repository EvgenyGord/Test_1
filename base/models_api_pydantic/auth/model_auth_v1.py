from pydantic import BaseModel, StrictInt, StrictStr, StrictBool


class AuthorizedResponseSuccess(BaseModel):
    value: StrictBool


class AuthorizedResponseError(BaseModel):
    code: StrictInt
    message: StrictStr
