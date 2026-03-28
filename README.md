# Turkey-vs-Romania-Shot-Analysis-Dashboard

turkey-vs-romania-shot-analysis-dashboard/
│
├── app1.py          👈 your Streamlit app
├── shots1.csv       👈 your data
├── requirements.txt 👈 CREATE IT HERE
├── README.md

## Live Demo: (https://turkey-vs-romania-shot-analysis-dashboard-a9e3n7hqk8jhpw2wdzuy.streamlit.app/)
## Objective

Analyze shot patterns and efficiency in the World Cup Qual. UEFA Playoffs match between Turkey and Romania using event data.

## Data Used
Shot-level event data (x, y coordinates)
Shot outcomes: goal, miss, block, save, post
Player and situation data (assisted, corner, free-kick)
## Key Findings
Turkey attempted 16 shots vs Romania’s 6, indicating territorial dominance
Despite higher volume, Turkey recorded only 1 goal, highlighting low efficiency
Romania’s shots were limited but came from slightly better positions
Turkey had 4 blocked shots, suggesting Romania defended compactly
## Visuals
Shot Map (Turkey)
Displays shot locations on a real pitch
Includes distance-to-goal annotations
Color-coded by shot outcome
Shot Map (Romania)
Adjusted for attacking direction
Reveals deeper shot locations and fewer attempts

👉 (Include your screenshot in /assets and display it)

## Data Challenge & Solution (THIS IS YOUR EDGE)

Problem:
There was a mismatch between raw data and visualization:

Romania had 3 blocked shots
Only 2 appeared on the shot map

Root Cause:

Not overlapping points ❌
Data filtering & plotting inconsistencies ✅

Solution:

Verified data using grouped counts
Standardized shot_type values
Ensured consistent transformation before plotting
df['shot_type'] = df['shot_type'].str.lower().str.strip()

## This ensured data integrity between analysis and visualization

## Tactical Implications
Turkey
Needs to improve shot quality rather than volume
High number of blocked shots suggests predictable attacking patterns
Could benefit from wider play or quicker ball circulation
Romania
Effective defensive structure limiting clear chances
Should improve attacking transitions to increase shot volume
## Tools Used
Python (Pandas, NumPy)
Matplotlib
mplsoccer
Streamlit

## requirements.txt
streamlit==1.32.0
pandas==2.2.2
matplotlib==3.8.4
numpy==1.26.4
mplsoccer==1.2.4
