import pandas as pd
from prophet import Prophet


class AIDemandForecast:

    def __init__(self, data_path):

        self.data_path = data_path
        self.model = Prophet()

    def load_data(self):

        df = pd.read_csv(self.data_path)

        # Prophet richiede colonne specifiche
        df = df.rename(columns={
            "date": "ds",
            "rooms_sold": "y"
        })

        return df

    def train_model(self):

        df = self.load_data()

        self.model.fit(df)

        return df

    def forecast(self, days=30):

        future = self.model.make_future_dataframe(periods=days)

        forecast = self.model.predict(future)

        return forecast
