# SPDX-License-Identifier: AGPL-3.0-only
"""Currency audit, EU norms: latest consolidated versions per CELEX from the Publications Office SPARQL."""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

ENDPOINT = "https://publications.europa.eu/webapi/rdf/sparql"
QUERY = """PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?date WHERE {{
  ?work cdm:resource_legal_id_celex "{celex}"^^xsd:string .
  ?cons cdm:act_consolidated_consolidates_resource_legal ?work .
  ?cons cdm:act_consolidated_date ?date .
}} ORDER BY DESC(?date) LIMIT 3"""


def latest_versions(celex: str) -> list[str]:
    query = {"query": QUERY.format(celex=celex), "format": "application/sparql-results+json"}
    params = urllib.parse.urlencode(query)
    request = urllib.request.Request(f"{ENDPOINT}?{params}", headers={"User-Agent": "curset-currency-audit"})
    with urllib.request.urlopen(request, timeout=90) as response:
        rows = json.load(response)["results"]["bindings"]
    return [row["date"]["value"] for row in rows]


if __name__ == "__main__":
    print(json.dumps({celex: latest_versions(celex) for celex in sys.argv[1:]}, indent=1))
