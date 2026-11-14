# Search and autocomplete

An online marketplace lists 40 million products. Shoppers type into a search box and expect suggestions after every keystroke, then expect relevant, stable result pages when they submit. The catalogue lives in Elasticsearch, with the product database as the source of truth.

The search team has three jobs to design:

- Autocomplete. The title field must complete partially typed words and phrases within a few milliseconds. The team compares a `search_as_you_type` field with its shingle subfields, a field mapped as `completion` for the completion suggester, and the term suggester for misspellings.
- Relevance. Results are ranked with the default similarity of Elasticsearch, and the team wants to understand how term frequency, document frequency and document length affect scores, and which parameters tune them.
- Pagination. Some users, and some export jobs, page through tens of thousands of hits. The team must keep pages consistent while documents are indexed and refreshed.

An inverted index stores the dictionary of terms and a posting list for each term, and the query text is analysed in the same way as the indexed text.
