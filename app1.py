import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import numpy as np

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("shots1.csv")

# Create team label
df['team'] = df['team_home'].apply(lambda x: 'Turkey' if x else 'Romania')

# -----------------------------
# TITLE
# -----------------------------
st.title("⚽ Turkey vs Romania - Shot Analysis Dashboard")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

team_filter = st.sidebar.selectbox("Select Team", ["All", "Turkey", "Romania"])
shot_filter = st.sidebar.selectbox("Shot Type", ["All"] + list(df['shot_type'].unique()))

# Apply filters
filtered_df = df.copy()

if team_filter != "All":
    filtered_df = filtered_df[filtered_df['team'] == team_filter]

if shot_filter != "All":
    filtered_df = filtered_df[filtered_df['shot_type'] == shot_filter]

# -----------------------------
# METRICS
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Shots", len(filtered_df))
col2.metric("Goals", len(filtered_df[filtered_df['shot_type'] == 'goal']))
col3.metric("On Target", len(filtered_df[filtered_df['shot_type'].isin(['goal', 'save'])]))

st.write(filtered_df[filtered_df['shot_type'] == 'block'])
# -----------------------------
# SHOT MAP (FIXED)
# -----------------------------
st.subheader("📍 Shot Map (With Distance)")

pitch = Pitch(
    pitch_type='statsbomb',
    pitch_color='#dbe2b0',
    line_color='white'
)

fig, ax = pitch.draw(figsize=(10, 6))

plot_df = filtered_df.copy()

# Flip Romania so both attack same direction
if team_filter == "Romania":
    plot_df['x'] = 120 - plot_df['x']
    plot_df['y'] = 80 - plot_df['y']

# ✅ CREATE DISTANCE HERE (IMPORTANT FIX)
plot_df['distance'] = np.sqrt(
    (120 - plot_df['x'])**2 + (40 - plot_df['y'])**2
).round(1)

# Colors
shot_colors = {
    "goal": "green",
    "miss": "red",
    "block": "orange",
    "save": "purple",
    "post": "blue"
}

# Plot shots
for _, row in plot_df.iterrows():
    ax.scatter(
        row['x'], row['y'],
        color=shot_colors.get(row['shot_type'], "black"),
        s=120,
        edgecolors='black',
        alpha=0.9
    )

    # Distance label (now works)
    ax.text(
        row['x'] + 1,
        row['y'] + 1,
        f"{row['distance']}m",
        fontsize=8,
        color='black'
    )

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Goal', markerfacecolor='green', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Miss', markerfacecolor='red', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Block', markerfacecolor='orange', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Post', markerfacecolor='blue', markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Save', markerfacecolor='purple', markeredgecolor='black')
]

ax.legend(handles=legend_elements, title="Shot Outcome", loc="upper right")

ax.set_title("Shot Map with Distance to Goal")

st.pyplot(fig)
# -----------------------------
# PLAYER ANALYSIS
# -----------------------------
st.subheader("👤 Player Shots")

player_shots = filtered_df['player'].value_counts().reset_index()
player_shots.columns = ['Player', 'Shots']

st.dataframe(player_shots)

# -----------------------------
# SITUATION ANALYSIS
# -----------------------------
st.subheader("⚙️ Shot Situations")

situation_counts = filtered_df['situation'].value_counts()

st.bar_chart(situation_counts)

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("🧠 Key Insights")

st.markdown("""
- Turkey dominates shot volume but struggles with efficiency  
- Romania creates limited chances under pressure  
- Attacking play is centralized around key players  
- Many shots come from low-quality situations  
""")