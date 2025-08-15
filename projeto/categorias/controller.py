from uuid import uuid4
from fastapi import APIRouter, Body, status
from pydantic import UUID4
from projeto.categorias.models import CategoriaModel
from projeto.categorias.schemas import CategoriaIn, CategoriaOut
from projeto.contrib.dependences import DatabaseDepency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
        '/', summary='Criar nova categoria',
        status_code=status.HTTP_201_CREATED,
        response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDepency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump)

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out

@router.get(
    '/',
    summary='Consultar categoria',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(
    db_session: DatabaseDepency, 
) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get(
    '/{id}',
    summary='Consultar uma categoria pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(
    id: UUID4,
    db_session: DatabaseDepency, 
) -> CategoriaOut:
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))
                               ).scalars().all()
    
    return categoria