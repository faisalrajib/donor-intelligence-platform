import great_expectations as ge
import pandas as pd

def validate_data(features_dict):
    df = pd.DataFrame(features_dict)
    ge_df = ge.from_pandas(df)

    ge_df.expect_column_values_to_not_be_null('donor_id')
    ge_df.expect_column_values_to_be_between('donor_score', 0, 1)

    results = ge_df.validate()
    if not results['success']:
        raise ValueError('Data quality checks failed')

    return df
