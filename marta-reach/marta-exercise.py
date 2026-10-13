# ============================================================
# MARTA Reach pilot data — Python + Excel exercise
# 700 ride requests, one week (June 2024). Mirrors the real work:
# analyze pilot data -> find trends -> scheduling recommendation.
#
# Setup (run once in terminal):  pip install pandas openpyxl
# Put marta-reach-rides.xlsx in the same folder as this file.
# ============================================================

import pandas as pd

df = pd.read_excel("marta-reach-rides.xlsx", sheet_name="rides")
# Columns: ride_id, date, request_hour, pickup_zone, dropoff_hub,
#          wait_min, ride_min, fare_usd, vehicle_id


# Q1: How many rides total? How many unique vehicles?
# (Hint: len(df), df["vehicle_id"].nunique())


# Q2: Which request_hour has the most ride requests?
# (Hint: df["request_hour"].value_counts() — this is the
#  "identify peak demand periods" step from the real project.)


# Q3: Average wait_min per pickup_zone. Which zone waits longest?
# (Hint: df.groupby("pickup_zone")["wait_min"].mean())


# Q4: Peak hours are 7-9 and 17-19. What's the average wait in
# peak hours vs off-peak? How big is the gap?
# (Hint: make a peak column with .isin([7,8,9,17,18,19]),
#  then groupby it.)


# Q5: The recommendation. In one comment, write the scheduling
# recommendation this data supports (which zones, which hours,
# what should change). Then write your Q2-Q4 summary tables to
# a NEW sheet called "findings" in the same Excel file.
# (Hint: pd.ExcelWriter with mode="a", or to_excel with
#  sheet_name="findings".)
