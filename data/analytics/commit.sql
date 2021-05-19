MERGE analytics.commit
USING (
    SELECT
        commit
        ,tree
        ,parent
        ,author.name AS author_name
        ,author.time_sec AS author_timesec
        ,committer.name AS committer_name
        ,committer.time_sec AS committer_time_sec
        ,subject
        ,message
        ,repo_name
        ,difference_truncated
    FROM `bigquery-public-data.github_repos.commits`
)
ON FALSE
WHEN NOT MATCHED THEN
    INSERT ROW
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
