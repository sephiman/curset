# Agentic diagnostics platform and enterprise AI gateway

A cloud company builds an internal platform in which diagnostic agents investigate production incidents. An agent reads alerts, fetches logs and dashboards, and proposes a fix to the on-call engineer. The agents reach internal systems through tools exposed by Model Context Protocol (MCP) servers, and all calls to language models and to tools go through one enterprise AI gateway.

The gateway has to enforce the company's rules in one place:

- Tool access. Agents call tools with `tools/call` requests. The MCP servers use an HTTP-based transport, so the access token is checked on every request, and a call that needs more permission gets a scope challenge.
- An MCP proxy. One proxy server fronts a third-party ticketing API for all agents, using a static client ID and a consent screen, so it must guard against confused deputy attacks and token passthrough.
- Content risks. Agents read logs, tickets and web pages written by others. Hidden instructions in that content could steer the model, and sensitive data such as personal data must not leak through answers.
- Verification. The security team plans adversarial testing of the whole chain.
