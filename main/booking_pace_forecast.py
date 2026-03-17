import pandas as pd


class BookingPaceForecast:

    def __init__(self, data_path):

        self.data_path = data_path

    def load_data(self):

        df = pd.read_csv(self.data_path)

        return df

    def calculate_lead_time(self):

        df = self.load_data()

        df["booking_date"] = pd.to_datetime(df["booking_date"])
        df["arrival_date"] = pd.to_datetime(df["arrival_date"])

        df["lead_time"] = (df["arrival_date"] - df["booking_date"]).dt.days

        return df

    def booking_pace(self):

        df = self.calculate_lead_time()

        pace = df.groupby("arrival_date").size().reset_index(name="bookings")

        return pace
