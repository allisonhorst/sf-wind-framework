from datetime import date, timedelta
import pandas as pd
import sys

todaySys = date.today()
yesterdaySys = todaySys - timedelta(days = 1)

today = todaySys.strftime("%Y%m%d")
yesterday = yesterdaySys.strftime("%Y%m%d")

url="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date="+yesterday+"&end_date="+today+"&station=9414290&product=wind&time_zone=lst_ldt&units=english&application=DataAPI_Sample&format=csv"

windDataRaw=pd.read_csv(url)
windData=windDataRaw.rename(columns={" Direction": "windDirAngle", " Direction.1": "windDirAbb"})

windData.to_csv(sys.stdout)