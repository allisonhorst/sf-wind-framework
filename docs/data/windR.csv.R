library(readr)
library(dplyr)

today <- format(Sys.Date(), "%Y%m%d")
last_week <- format(Sys.Date() - 1, "%Y%m%d")
url <- paste0("https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=", last_week, "&end_date=", today, "&station=9414290&product=wind&time_zone=lst_ldt&units=english&application=DataAPI_Sample&format=csv")
wind_data <- read_csv(url) |>
  rename(windDirAngle = Direction...3, windDirAbb = Direction...4)

cat(format_csv(wind_data))
