from extractor import Extractor


def test_clean_query(query_user_activity, cleaned_user_activity):
    schema = "reporting"
    dir_report = f"data/{schema}"
    extractor = Extractor(script_dir=dir_report, schema=schema)
    txt_remove = [
        f"MERGE {schema}.user_activity USING (",
        ") ON FALSE WHEN NOT MATCHED THEN "
        "INSERT ROW WHEN NOT MATCHED BY SOURCE THEN "
        "DELETE",
    ]
    cleaned_query = extractor.clean_query(
        query=query_user_activity, str_to_remove=txt_remove
    )
    assert cleaned_query == cleaned_user_activity
