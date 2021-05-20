MERGE analytics.committer
USING (
    SELECT
        committer.name AS name
        ,committer.email AS email
        ,committer.time_sec AS time_sec
        ,committer.tz_offset AS tz_offset
        ,committer.date.seconds AS date_seconds
        ,committer.date.nanos AS date_nanos
    FROM github_repos.commits
)
ON FALSE
WHEN NOT MATCHED THEN
    INSERT ROW
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
