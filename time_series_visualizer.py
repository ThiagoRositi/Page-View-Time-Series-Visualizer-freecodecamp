import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col="date")

# Clean data
suplim = df.shape[0]*0.975
inflim = df.shape[0]*0.025
df.sort_values(by="value",inplace=True)
df = df.iloc[round(inflim):round(suplim)]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(16, 5))
    plt.plot(df, c="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
     # Draw bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    years = [2016, 2017, 2018, 2019]
    data = np.zeros([12, 4])

    for i in range(12):
        for j, year in enumerate(years):
            t = df[df.index.year == year]
            data[i][j] = t[t.index.month == i].value.mean()

    x = np.arange(len(years))
    width = 0.7
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(8)
    for i, month in enumerate(data):
        ax.bar(x - (width * (12 - i) / 12), data[i], width / 12, label=months[i])

    ax.set_ylabel("Average Page Views")
    ax.set_xlabel("Years")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(title='Months')
    
    # # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['year'] = df_box['year'].astype(int)
    df_box['value'] = df_box['value'].astype(int)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(data=df_box, x="year",width=1, y="value", ax=axes[0], palette="bright", fliersize=1,saturation=0.6, legend=False)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    data = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month",width=1, y="value", ax=axes[1], palette="pastel", fliersize=1, saturation=2, order=data, legend=False)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
