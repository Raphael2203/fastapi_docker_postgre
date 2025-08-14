from typing import Annotated
from pydantic import Field
from projeto.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Categoria', example='Scale', max_length=10)]   