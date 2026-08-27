def add_features(df):

    df['spend_income_ratio'] = (
        df['monthly_spend'] / df['income']
    )

    df['rolling_spend_mean'] = (
        df['monthly_spend'].rolling(3).mean()
    )

    df['region_frequency'] = (
        df['region'].map(
            df['region'].value_counts(normalize=True)
        )
    )

    return df