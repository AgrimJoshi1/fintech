def financial_analytics(data):

    stability_score = data.work_consistency * 100

    volatility_value = data.daily_income_variation

    if volatility_value < 0.2:
        volatility = "LOW"

    elif volatility_value < 0.5:
        volatility = "MEDIUM"

    else:
        volatility = "HIGH"

    repayment_confidence = 100 - (
        volatility_value * 100
    )

    return {
        "income_stability": round(stability_score, 2),
        "volatility": volatility,
        "repayment_confidence": round(
            repayment_confidence, 2
        )
    }