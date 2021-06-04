import writer


def test_create_query_constraint(datasets, dir_file, query_constraint):
    query = writer.create_query_constraint(datasets=datasets, dir_file=dir_file)
    assert query == query_constraint


def test_create_query_node_import(datasets, dir_file, query_node_import):
    query = writer.create_query_node_import(datasets=datasets, dir_file=dir_file)
    assert query == query_node_import


def test_create_query_relationship(datasets, dir_file, query_rel):
    query = writer.create_query_relationship(datasets=datasets, dir_file=dir_file)
    assert query == query_rel
