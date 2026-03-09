import pandas as pd

def analyze_spending(file):

    df = pd.read_csv(file)

    income = df[df["amount"] > 0]["amount"].sum()
    expenses = df[df["amount"] < 0]["amount"].sum()

    burn_rate = abs(expenses)

    savings_rate = (income + expenses) / income * 100

    food_spend = abs(df[df["category"] == "Food"]["amount"].sum())
    shopping_spend = abs(df[df["category"] == "Shopping"]["amount"].sum())

    if shopping_spend > 300:
        personality = "Lifestyle Spender"
    elif savings_rate > 30:
        personality = "Wealth Builder"
    else:
        personality = "Balanced Spender"

    advice = "Consider reducing non-essential spending to improve savings."

    return personality, burn_rate, round(savings_rate,2), advice
