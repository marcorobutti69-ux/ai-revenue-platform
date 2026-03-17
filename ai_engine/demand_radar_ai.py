import pandas as pd


def run_demand_radar():

    bookings = pd.read_csv("datasets/bookings.csv")

    radar = []

    # esempio semplice: analisi per data
    grouped = bookings.groupby("date")["rooms_sold"].sum().reset_index()

    for _, row in grouped.iterrows():

        date = row["date"]
        rooms = row["rooms_sold"]

        if rooms > 80:
            radar.append({
                "date": date,
                "type": "High demand spike"
            })

        elif rooms < 20:
            radar.append({
                "date": date,
                "type": "Low demand period"
            })

        elif rooms > 60:
            radar.append({
                "date": date,
                "type": "Revenue opportunity"
            })

    return radar
