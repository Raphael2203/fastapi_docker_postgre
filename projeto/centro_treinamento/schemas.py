from typing import Annotated
from pydantic import Field
from projeto.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua do café, 21, ', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de treinamento', example='Raphael Brito', max_length=30)]