import exporter
import pandas.testing as pdt


def test_convert_dict_to_df(extracted_analytics, dict_as_df):
    df = exporter.convert_dict_to_df(data=extracted_analytics)
    pdt.assert_frame_equal(
        left=df.reset_index(drop=True), right=dict_as_df.reset_index(drop=True)
    )
