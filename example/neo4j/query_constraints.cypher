CREATE CONSTRAINT table_name_ConstraintReporting ON (r:Reporting)
ASSERT r.table_name IS UNIQUE;
CREATE CONSTRAINT table_name_ConstraintAnalytics ON (a:Analytics)
ASSERT a.table_name IS UNIQUE;
CREATE CONSTRAINT table_name_ConstraintGitHub_Repos ON (g:GitHub_Repos)
ASSERT g.table_name IS UNIQUE;
