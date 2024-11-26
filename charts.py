import matplotlib.pyplot as plt
import re
import pandas as pd

WITHOUT_LOSERS = False

# Read the markdown file
with open("readme.md", "r") as file:
    content = file.read()

# Regular expression to extract language and real time
pattern = re.compile(r"## `(.*?)`.*?real\s+(\d+m\d+,\d+s)", re.DOTALL)

# Find all matches
matches = pattern.findall(content)

# Extract language names and real times
languages = []
real_times = []

for match in matches:
    language = match[0]
    real_time = match[1]

    # Convert real time to seconds
    minutes, seconds = real_time.split("m")
    seconds = seconds.replace(",", ".").replace("s", "")
    total_seconds = int(minutes) * 60 + float(seconds)

    languages.append(language)
    real_times.append(total_seconds)

# Sort languages and real times by real times
sorted_indices = sorted(range(len(real_times)), key=lambda k: real_times[k])
sorted_languages = [languages[i] for i in sorted_indices]
sorted_real_times = [real_times[i] for i in sorted_indices]

# Calculate relative times
best_time = sorted_real_times[0]
relative_times = [time / best_time for time in sorted_real_times]

if WITHOUT_LOSERS:
    sorted_languages = sorted_languages[:-5]
    sorted_real_times = sorted_real_times[:-5]
    relative_times = relative_times[:-5]

# Create a comparison DataFrame
comparison_data = pd.DataFrame(index=sorted_languages, columns=sorted_languages)

# Fill the DataFrame with relative performance data
for i, lang1 in enumerate(sorted_languages):
    for j, lang2 in enumerate(sorted_languages):
        if i == j:
            comparison_data.loc[lang1, lang2] = 1.0  # Self comparison
        else:
            comparison_data.loc[lang1, lang2] = round(
                relative_times[i] / relative_times[j], 3
            )

# Save the comparison DataFrame to a CSV file
csv_filename = "benchmark_comparison_results.csv"
comparison_data.to_csv(csv_filename)

# Plot the original chart
plt.figure(figsize=(10, 6))
bars = plt.barh(sorted_languages, sorted_real_times, color="skyblue")
plt.xlabel("Time (seconds)")
plt.title("Absolute Benchmark Results")
plt.gca().invert_yaxis()  # Invert y-axis to show the best result at the top
# Add values to the bars
for bar, value in zip(bars, sorted_real_times):
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}",
        va="center",
        ha="left",
    )
plt.show()

# Plot the relative chart
plt.figure(figsize=(10, 6))
bars = plt.barh(sorted_languages, relative_times, color="lightgreen")
plt.xlabel("Relative Time (best result = 1)")
plt.title("Relative Benchmark Results")
plt.gca().invert_yaxis()  # Invert y-axis to show the best result at the top

# Add values to the bars
for bar, value in zip(bars, relative_times):
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}",
        va="center",
        ha="left",
    )

plt.show()
