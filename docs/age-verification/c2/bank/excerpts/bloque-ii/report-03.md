# Blind excerpt check — bloque-ii, batch 03

Labels verified against the saved file: HTML as rendered text (tags stripped, entities decoded, whitespace runs collapsed),
`.txt` with line wraps joined by one space. Every label below was found exactly once by `grep -F` on that rendering.

n | key | verdict | label or none: reason | flags
---|---|---|---|---
121 | m02-l12-q190 | no | Errors detected may be reported via the Internet Control Message Protocol (ICMP) [3] which is implemented in the internet protocol module. | excerpt is another paragraph of 1.4
122 | m02-l12-q191 | no | none: spread — «text based conferencing» and «the client-server model» are in two separate paragraphs of 1. INTRODUCTION | excerpt is the Abstract
123 | m02-l12-q193 | yes | |
124 | m02-l12-q194 | yes | |
125 | m02-l12-q196 | no | none: spread — «The commands which may only be used by channel operators are:» and the «KICK - Eject a client from the channel» line are separate paragraphs (the list line has no punctuation) | excerpt is the paragraph before the list
126 | m02-l12-q206 | yes | |
127 | m02-l12-q209 | no | Technical direction and standards (W3C Recommendations) require review by W3C Members – large and small. | excerpt stops before «Decisions are taken by consensus.» (itself only five words); the label is in the same paragraph
128 | m02-l12-q210 | no | W3C standards may be used by anyone at no cost: if they were not free, developers would ignore them. | excerpt is the paragraph before the «Royalty-free to boost adoption» block
129 | m02-l12-q211 | yes | |
130 | m02-l12-q212 | no | none: no admissible label — the aim is only in the site tagline «Strategies, standards, resources to make the Web accessible to people with disabilities» (header and footer furniture, no final punctuation) | no excerpt
131 | m02-l12-q213 | yes | |
132 | m02-l12-q214 | yes | |
133 | m02-l12-q216 | yes | |
134 | m02-l12-q217 | no | All W3C standards are reviewed for accessibility support by the Accessible Platform Architectures (APA) Working Group. | excerpt is the Introduction paragraph
135 | m02-l12-q218 | yes | |
136 | m02-l12-q229 | yes | |
137 | m02-l12-q232 | yes | |
138 | m02-l12-q233 | no | none: heading only — «Herramienta de blog, plataforma de publicación y CMS» appears only in the page title (and og:title), not in the body | no excerpt
139 | m02-l12-q261 | no | none: spread — the arrow-key highlight step and «Presione Tab para seleccionar document.» (five words) are separate steps | excerpt is page furniture («Comentarios»)
140 | m02-l12-q263 | no | Si es necesario, haga clic en DevTools para darle el foco y, a continuación, presione Esc para abrir la consola. | excerpt is page furniture («Comentarios»)
141 | m02-l12-q292 | no | Beginning with the first three networks (ARPANET, Packet Radio, and Packet Satellite) and their initial research communities, the experimental environment has grown to incorporate essentially every form of network and a very broad-based research and development community. | excerpt is the preceding paragraph (DARPA contracts)
142 | m02-l12-q294 | no | Thus a 32 bit IP address was used of which the first 8 bits signified the network and the remaining 24 bits designated the host on that network. | excerpt is the section's first paragraph
143 | m02-l12-q295 | no | As the number of networks in the Internet exploded, this initial design could not expand as necessary, so it was replaced by a hierarchical model of routing, with an Interior Gateway Protocol (IGP) used inside each region of the Internet, and an Exterior Gateway Protocol (EGP) used to tie the regions together. | excerpt is the section's first paragraph
144 | m02-l12-q296 | no | On the NSFNET Backbone – the national-scale segment of the NSFNET – NSF enforced an “Acceptable Use Policy” (AUP) which prohibited Backbone usage for purposes “not in support of Research and Education. | excerpt is the section's first paragraph; the sentence on the page ends «.”», the label stops at the «.» before the closing quote
145 | m02-l12-q299 | no | That implementation was fully interoperable with other TCPs, but was tailored to the application suite and performance objectives of the personal computer, and showed that workstations, as well as large time-sharing systems, could be a part of the Internet. | excerpt is the DARPA contracts paragraph
146 | m02-l12-q300 | no | “Internet” refers to the global information system that — (i) is logically linked together by a globally unique address space based on the Internet Protocol (IP) or its subsequent extensions/follow-ons; (ii) is able to support communications using the Transmission Control Protocol/Internet Protocol (TCP/IP) suite or its subsequent extensions/follow-ons, and/or other IP-compatible protocols; and (iii) provides, uses or makes accessible, either publicly or privately, high level services layered on the communications and related infrastructure described herein. | excerpt shows the paragraph's first two sentences only, before the definition
147 | m02-l12-q301 | no | The following year, the W3C membership decided to stop evolving HTML and instead begin work on an XML-based equivalent, called XHTML. | the label's paragraph says «The following year»; 1998 follows only from the previous paragraph (HTML4, 1997); excerpt has «This section is non-normative.» plus the DOM Level 1 paragraph
148 | m02-l12-q302 | yes | | excerpt glues «This section is non-normative.» to the paragraph
149 | m02-l12-q303 | no | In 2011, however, the groups came to the conclusion that they had different goals: the W3C wanted to publish a "finished" version of "HTML5", while the WHATWG wanted to continue working on a Living Standard for HTML, continuously maintaining the specification rather than freezing it in a state with known problems, and adding new features as needed to evolve the platform. | excerpt is the section's first paragraph
150 | m02-l12-q304 | no | The WHATWG was based on several core principles, in particular that technologies need to be backwards compatible, that specifications and implementations need to match even if this means changing the specification rather than the implementations, and that specifications need to be detailed enough that implementations can achieve complete interoperability without reverse-engineering each other. | excerpt is the section's first paragraph
151 | m02-l12-q305 | no | Authors are reminded that the processing for XML and HTML differs; in particular, even minor syntax errors will prevent a document labeled as XML from being rendered fully, whereas they would be ignored in the HTML syntax. | excerpt is the sample markup (code), not prose
152 | m02-l12-q306 | no | A DOM tree is an in-memory representation of a document. | excerpt is the sample markup (code), not prose
153 | m02-l12-q307 | no | The document element of this tree is the html element, which is the element always found in that position in HTML documents. | excerpt is the sample markup (code), not prose
154 | m02-l12-q308 | yes | |
155 | m02-l12-q309 | no | Authors are also encouraged to make their applications degrade gracefully in the absence of scripting support. | excerpt is the paragraph before
156 | m02-l12-q310 | no | The noscript element represents nothing if scripting is enabled, and represents its children if scripting is disabled. | no excerpt
157 | m02-l12-q311 | no | For external classic scripts, if the async attribute is present, then the classic script will be fetched in parallel to parsing and evaluated as soon as it is available (potentially before parsing completes). | excerpt is page furniture («✔MDN»); the attribute list line «async — Execute script when available, without blocking while fetching» has no final punctuation, so the label is the prose sentence
158 | m02-l12-q317 | yes | |

## Counts

- items: 38
- yes: 13
- no with a label: 20
- no with none: 5
  - spread: 3 (122, 125, 139)
  - heading only: 1 (138)
  - no admissible label (fact only in unpunctuated site tagline): 1 (130)
