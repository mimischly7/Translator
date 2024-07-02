# Translation

This sub-project handles the step in our pipeline where we read data from the formatted Iceberg tables,
produce text documents from them, and store them to one or more storage endpoints like a vector database or
a keyword search engine; in this case, we will be storing to `QDrant` for semantic search (vector embeddings)
and to `ElasticSearch` for keyword search.
