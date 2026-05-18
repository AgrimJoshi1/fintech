from fastapi import APIRouter

from models.schemas import UserFinancialData
from services.risk_engine import calculate_risk

router = APIRouter()


@router.post("/predict-loan")
def predict_loan(data: UserFinancialData):

    result = calculate_risk(data)

    loan_amount = (
        data.income * result["multiplier"]
    )

    return {
        "eligible_loan": round(loan_amount, 2),
        "risk": result["risk"],
        "confidence": result["confidence"]
    }