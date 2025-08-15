from fastapi import APIRouter, Body, status
from projeto.atleta.schemas import AtletaIn
from projeto.contrib.dependences import DatabaseDepency

router = APIRouter()

@router.post(
        '/', summary='Criar novo atleta',
        status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDepency, 
    atleta_in: AtletaIn = Body(...)
):
    pass