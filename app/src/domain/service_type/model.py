from pydantic import BaseModel


class ServiceType(BaseModel):
    code: str
    name: str
