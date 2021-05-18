MERGE analytics.user
USING (
    SELECT DISTINCT
        name
        ,email
        ,'author' AS user_type
    FROM analytics.author
    UNION
    SELECT DISTINCT
        name
        ,email
        ,'committer' AS user_type
    FROM analytics.committer)
ON FALSE
WHEN NOT MATCHED THEN
    INSERT ROW
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
