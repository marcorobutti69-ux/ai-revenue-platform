import pandas as pd


def optimize_total_revenue(file_path):

    data = pd.read_csv(file_path)

    total_rooms = data["rooms_revenue"].sum()
    total_fnb = data["fnb_revenue"].sum()
    total_spa = data["spa_revenue"].sum()
    total_events = data["events_revenue"].sum()
    total_excursions = data["excursions_revenue"].sum()
    total_transfers = data["transfer_revenue"].sum()

    total_revenue = (
        total_rooms +
        total_fnb +
        total_spa +
        total_events +
        total_excursions +
        total_transfers
    )

    report = {}

    report["rooms_revenue"] = float(total_rooms)
    report["fnb_revenue"] = float(total_fnb)
    report["spa_revenue"] = float(total_spa)
    report["events_revenue"] = float(total_events)
    report["excursions_revenue"] = float(total_excursions)
    report["transfer_revenue"] = float(total_transfers)
    report["total_revenue"] = float(total_revenue)

    return report
