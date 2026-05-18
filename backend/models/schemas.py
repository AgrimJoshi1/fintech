from pydantic import BaseModel
from typing import List


class UserFinancialData(BaseModel):
    income: float
    expenses: float
    missed_payments: int
    work_consistency: float
    daily_income_variation: float


class InsuranceInput(BaseModel):
    income_drop: float
    rainfall: float


class LoanResponse(BaseModel):
    eligible_loan: float
    risk: str
    confidence: float


class EMIResponse(BaseModel):
    emi: float
    message: str


class InsuranceResponse(BaseModel):
    payout_triggered: bool
    payout_amount: float


class AnalyticsResponse(BaseModel):
    risk_score: float
    income_stability: float
    volatility: str
    repayment_confidence: float
    alerts: List[str]