from fastapi import APIRouter

from models.schemas import UserFinancialData
from services.emi_engine import calculate_emi

router = APIRouter()


@router.post("/adjust-emi")
def adjust_emi(data: UserFinancialData):

    emi = calculate_emi(data.income)

    return {
        "emi": emi,
        "message": "Adaptive EMI calculated"
    }