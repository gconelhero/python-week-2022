from typing import Optional, List
from fastapi import FastAPI, Response, status
from beerlog.core import get_beers_from_database
from beerlog.serializers import BeerIn, BeerOut
from beerlog.database import get_session
from beerlog.models import Beer


api = FastAPI(title="beerlog ")


@api.get("/beers", response_model=List[BeerOut])
async def list_beers(style: Optional[str] = None):
    """Lists beers from the database"""
    print("TESTE")
    beers = get_beers_from_database(style)
    return beers


@api.post("/beers", response_model=BeerIn)
async def add_beer(beer_in: BeerIn, response: Response):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        print(beer)
        session.add(beer)
        session.commit()
        session.refresh(beer)

    response.status_code = status.HTTP_201_CREATED
    return beer
