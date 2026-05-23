import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/skill_counts.csv")

df = df.sort_values("Count", ascending=False)

plt.figure(figsize=(12,6))

plt.bar(df["Skill"][:10], df["Count"][:10])

plt.xticks(rotation=45)

plt.title("Top 10 Skills in Current Market")

plt.tight_layout()

plt.savefig("output/top_10_skills.png")

plt.show()

print("Trend analysis completed!")
