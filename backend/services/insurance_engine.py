def insurance_trigger(income_drop, rainfall):

    payout = False
    payout_amount = 0

    if income_drop > 40:
        payout = True
        payout_amount = 5000

    if rainfall > 120:
        payout = True
        payout_amount = 7000

    return {
        "payout_triggered": payout,
        "payout_amount": payout_amount
    }