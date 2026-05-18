from fastapi import APIRouter

from models.schemas import UserFinancialData

from services.risk_engine import (
    calculate_risk
)

from services.analytics_engine import (
    financial_analytics
)

from services.insight_engine import (
    generate_alerts
)

router = APIRouter()


@router.post("/analytics")
def analytics(data: UserFinancialData):

    risk_data = calculate_risk(data)

    analytics_data = financial_analytics(data)

    alerts = generate_alerts(
        risk_data["risk_score"],
        analytics_data["income_stability"],
        analytics_data["volatility"]
    )

    return {
        "risk_score":
            risk_data["risk_score"],

        "income_stability":
            analytics_data["income_stability"],

        "volatility":
            analytics_data["volatility"],

        "repayment_confidence":
            analytics_data[
                "repayment_confidence"
            ],

        "alerts": alerts
    }