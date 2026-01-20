Title: Use PostgreSQL as Primary Database

Status: Approved

Context: Our application requires a relational database to handle structured data with strong consistency. Options considered included MySQL, MongoDB, and PostgreSQL.

Decision: PostgreSQL will be used as the primary database due to its reliability, support for complex queries, and strong community support.

Consequences:

Team must maintain PostgreSQL instances and backups.

Future developers need to be familiar with SQL and PostgreSQL-specific features.

Migration from another database would require data transformation scripts.
