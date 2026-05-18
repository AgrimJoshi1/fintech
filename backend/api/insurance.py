from fastapi import APIRouter

from models.schemas import InsuranceInput
from services.insurance_engine import (
    insurance_trigger
)

router = APIRouter()


@router.post("/insurance-trigger")
def insurance_check(data: InsuranceInput):

    result = insurance_trigger(
        data.income_drop,
        data.rainfall
    )

    return result