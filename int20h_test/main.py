import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the data set into a pandas dataframe
    df = pd.read_csv("int20h-ds-test-dataset.csv")

    cancel_df = df[df['event_name'] == 'Subscription Premium Cancel']

    # Aggregate the count of each event for each user
    agg_df = df.groupby('userid')['event_name'].value_counts().unstack().fillna(0)

    # Join the aggregated data with the filtered data from step 1
    merged_df = cancel_df.merge(agg_df, left_on='userid', right_index=True)

    # Calculate the correlation between each event and Subscription Premium Cancel
    corr = merged_df.corr()
    cancel_corr = corr['Subscription Premium Cancel']

    # Plot the correlations using a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(cancel_corr.sort_values(ascending=False).to_frame(), annot=True)
    plt.show()

    # Get the events, event properties, or user properties with the highest or lowest correlation
    events_with_high_correlation = cancel_corr.sort_values(ascending=False).head(10)
    events_with_low_correlation = cancel_corr.sort_values().head(10)

    print("Events, event properties, or user properties with high correlation with account cancellation:")
    print(events_with_high_correlation)

    print("\nEvents, event properties, or user properties with low correlation with account cancellation:")
    print(events_with_low_correlation)

if __name__ == '__main__':
    main()