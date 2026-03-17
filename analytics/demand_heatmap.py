import pandas as pd
import plotly.express as px


class DemandHeatmap:

    def __init__(self, dataframe):

        self.df = dataframe


    def create_heatmap(self):

        df = self.df.copy()

        df["date"] = pd.to_datetime(df["date"])

        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day

        heatmap = px.density_heatmap(
            df,
            x="day",
            y="month",
            z="bookings",
            color_continuous_scale="YlOrRd",
            title="Demand Heatmap"
        )

        return heatmap
