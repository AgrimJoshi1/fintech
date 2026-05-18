def calculate_risk(data):

    expense_ratio = data.expenses / data.income

    risk_score = (
        (data.daily_income_variation * 40)
        + (data.missed_payments * 20)
        + (expense_ratio * 25)
        - (data.work_consistency * 15)
    )

    if risk_score < 30:
        risk = "LOW"
        multiplier = 2.5

    elif risk_score < 60:
        risk = "MEDIUM"
        multiplier = 2.0

    else:
        risk = "HIGH"
        multiplier = 1.2

    repayment_confidence = max(0, 100 - risk_score)

    return {
        "risk_score": round(risk_score, 2),
        "risk": risk,
        "multiplier": multiplier,
        "confidence": round(repayment_confidence, 2)
    }