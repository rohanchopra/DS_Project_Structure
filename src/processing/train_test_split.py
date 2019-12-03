from sklearn.model_selection import train_test_split


def tt_split(scaled_df, Y):
    return train_test_split(scaled_df, Y, test_size=0.3, random_state=0)


def ttv_split(scaled_df, Y):
    # TODO: Implement Test, train and validation split
    pass
