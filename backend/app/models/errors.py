from pydantic import BaseModel, Field


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")


class BaseIdentifiedError(BaseError):
    identifier: str = Field(..., descirption="Unique identifier which this error references to")


class NotFoundError(BaseIdentifiedError):
    pass


class AlreadyExistsError(BaseIdentifiedError):
    pass
