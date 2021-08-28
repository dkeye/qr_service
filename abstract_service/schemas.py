from pydantic import BaseModel


class CodeBase(BaseModel):
    code: str


class Code(CodeBase):
    is_activated: bool = False

    class Config:
        orm_mode = True
