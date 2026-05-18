def generate_alerts(
    risk_score,
    stability,
    volatility
):

    alerts = []

    if risk_score < 30:
        alerts.append(
            "Credit score improving"
        )

    if stability > 80:
        alerts.append(
            "Income stability strong"
        )

    if volatility == "HIGH":
        alerts.append(
            "Income volatility increasing"
        )

    if risk_score > 60:
        alerts.append(
            "High financial risk detected"
        )

    return alerts