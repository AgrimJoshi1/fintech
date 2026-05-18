def calculate_emi(income):

    if income > 60000:
        emi_ratio = 0.30

    elif income > 30000:
        emi_ratio = 0.22

    else:
        emi_ratio = 0.15

    emi = income * emi_ratio

    return round(emi, 2)