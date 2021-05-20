import pytest
import os
from extractor import Extractor


# run multiple times to ensure value ordering is preserved
# if not preserved, then test will fail
@pytest.mark.parametrize("execution_number", range(3))
def test_extract_table_dependencies_from_queries(
    execution_number, extracted_reporting, extracted_analytics
):
    schemes = ["analytics", "reporting"]
    extract = [extracted_analytics, extracted_reporting]

    for i, schema in enumerate(schemes):
        dir_report = f"data/{schema}"
        remove_txt = []
        for table in os.listdir(dir_report):
            table_name, _ = os.path.splitext(p=table)
            remove_txt.append(f"MERGE {schema}.{table_name} USING (")
        remove_txt.append(
            ") ON FALSE WHEN NOT MATCHED THEN "
            "INSERT ROW WHEN NOT MATCHED BY SOURCE THEN "
            "DELETE"
        )
        extractor = Extractor(script_dir=dir_report, schema=schema)
        output = extractor.extract_table_dependencies_from_queries(
            reference_datasets=["reporting", "analytics", "github_repos"],
            str_to_remove=remove_txt,
        )
        assert output == extract[i]
