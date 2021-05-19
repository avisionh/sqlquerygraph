MERGE analytics.author
USING (
    SELECT
        author.name AS name
        ,author.email AS email
        ,author.time_sec AS time_sec
        ,author.tz_offset AS tz_offset
        ,author.date.seconds AS date_seconds
        ,author.date.nanos AS date_nanos
    FROM `bigquery-public-data.github_repos.commits`
)
ON FALSE
WHEN NOT MATCHED THEN
    INSERT ROW
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
