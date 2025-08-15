import matplotlib.pyplot as plt
import numpy as np

gender_labels = ['Male', 'Female']
gender_counts = [250, 270]

ages = [
    22, 25, 25, 26, 28, 28, 29, 30, 31, 31, 32, 32, 33, 34, 35, 35,
    36, 36, 37, 38, 38, 39, 40, 40, 41, 42, 42, 43, 44, 45, 45, 46,
    47, 48, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
    23, 24, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42,
    43, 44, 45, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 62, 63, 65
]

def create_plots():
    fig, ax = plt.subplots()
    ax.bar(gender_labels, gender_counts, color=['#4BACC6', '#FF9999'])
    ax.set_title('Gender Distribution in Population', fontsize=16, pad=20)
    ax.set_xlabel('Gender', fontsize=12)
    ax.set_ylabel('Number of People', fontsize=12)
    for i, count in enumerate(gender_counts):
        ax.text(i, count + 2, str(count), ha='center', va='bottom', fontsize=10)
    plt.savefig('gender_distribution_bar_chart.png')
    plt.show()

    fig, ax = plt.subplots()
    bins = np.arange(min(ages), max(ages) + 11, 10)
    ax.hist(ages, bins=bins, edgecolor='black', rwidth=0.85, color='#4BACC6')
    ax.set_title('Age Distribution (Histogram)', fontsize=16, pad=20)
    ax.set_xlabel('Age Range', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    plt.savefig('age_distribution_histogram.png')
    plt.show()

if __name__ == "__main__":
    create_plots()
