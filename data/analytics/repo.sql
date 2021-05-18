MERGE analytics.repo
USING (
    SELECT
        a.repo_name
        ,a.author.name
        ,a.author.time_sec
        ,b.language.name AS language
        ,b.language.bytes AS repo_size
        ,c.license
    FROM `bigquery-public-data.github_repos.commits` AS a
    LEFT JOIN `bigquery-public-data.github_repos.languages` AS b
        ON a.repo_name = b.repo_name
    LEFT JOIN `bigquery-public-data.github_repos.licenses` AS c
        ON a.repo_name = c.repo_name)
ON FALSE
WHEN NOT MATCHED THEN
    INSERT ROW
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
