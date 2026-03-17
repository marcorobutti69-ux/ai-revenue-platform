from ai_engine.price_calendar_ai import generate_price_calendar


def scan_revenue_opportunities():

    calendar = generate_price_calendar(30)

    opportunities = []

    for day in calendar:

        price = day["recommended_price"]

        if price < 150:
            opportunities.append({
                "date": day["date"],
                "type": "Underpriced date",
                "action": "Consider increasing price"
            })

        elif price > 180:
            opportunities.append({
                "date": day["date"],
                "type": "Premium pricing window",
                "action": "High demand opportunity"
            })

    return opportunities
