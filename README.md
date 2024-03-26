# Demos and Basic Tutorials for KG Visualization Tools

This repo contains some example data, code, and resources related to my TWed talk on tools and methods for visualizing 
KG snippets.

## Scope

The purpose of this demo and content in this repo are to explore and discuss options for **visualizing** some KG or
small portion of a KG. Additional capabilities of various tools, like querying and analysis, are only discussed when
they are relevant to our ability to visualize things.

To support this, several different versions of KGs with different extends of "relevant" information have been curated,
and detailed in the next section.

## Data

The data contained in `data/` is formatted as `.ttl` files of KG snippets, related to my previous work on 
[event prediction using Wikidata](https://github.com/solashirai/WWW-EvCBR/). The entities and relations contained in
each file are based on Wikidata entries as of ~May 2023, and aim to provide some examples of KG snippets with varying
sizes and connectivity to demonstrate each tool's abilities. Note that only the direct property triples from Wikidata
are included, rather than the reified statements with qualifiers and sources.

Each of the files is based on our EvCBR method and its ability to predict properties about some new "effect" event
 which is caused by some "cause" event. In our examples, the cause is a protest in Iran. To perform predictions, EvCBR
 collects a number of similar past cause-effect event pairs, learns prediction paths based on these cases, then applies
 them to the new event to make predictions.
 
- `pred_path.ttl` contains triples about a new "cause" and "effect" event, as well as some relevant paths through the
 KG which were used to make predictions about the effect event's location. 
- `fc_mini.ttl` contains examples of 5 cause-effect events from the KG, which were determined by EvCBR as being similar 
 to our new protest event. A minimal number of properties, about the type and location of each event pair, is included.
- `fc_one.ttl` contains the same 5 cause-effect event pairs, but now includes _all_ outgoing edges for each event.
- `fc_three.ttl` is the largest file, and starts from the same 5 cause-effect event pairs and collects all outgoing
 edges within a 3-hop neighborhood. This file contains a significant amount of data compared to the other files, 
 consisting of 547,764 triples.
 
Each file contains `rdfs:label`s for entities as well as properties, which ideally would be utilized by visualization
tools. All other relations are using Wikidata's properties, so tools which rely on certain RDF or OWL conventions might
not be able to effectively utilize them (TODO - maybe make RDF versions of some files to demonstrate, replacing
wd:instanceof with rdf:type).

## Tools

Each tool included in this demonstration has a corresponding folder with its own README and tool details (and, if 
required, some additional scripts to make it work).
A rough breakdown of each tool is included in the following table.
For each column, `+` generally indicates positive attitude
 for a tool, `-` indicates negative attitude, and `~` indicates some qualified strengths or existence of tradeoffs.
 
Whereever possible, I also am focused on the perspective of using Python for these tools.

| Tool | Effort Required | Supports RDF | Automated Formatting | Interactive | Customizable | Notes | 
| - | - | - | - | - | - | - |
| Powerpoint | - | - | - | - | + | 100% manual effort |
| draw.io | - | - | - | - | + | Mostly manual effort, some importing possible |
| WebVOWL | ~ | ~ | + | + | - | Mainly aimed at ontology visualization |
| GraphDB | ~ | + | ~ | + | - | Well compatible with RDF, not the most visually appealing |
| sigma.js | x | x | x | x | x | TODO |
| Graphviz | x | x | x | x | x | TODO |
| Neo4J | ~ | - | + | + | - | Not suitable for RDF data |
| Ontograph (Protege) | ~ | + | ~ | ~ | - | Assumes ontology-like class structure, browsing capabilities seem limited |
| OWLViz (Protege) | - | + | - | - | - | Seems to be broken on windows |
| yWorks (yEd) | x | x | x | x | x | TODO |
| Cytoscape | x | x | x | x | x | TODO |
| Gephi | x | x | x | x | x | TODO |

This list is certainly not extensive -- there are many works out there that can be used to visualize graphs more 
generally, especially when they are set up in common graph formats such as those used by DOT, networkx, or igraph. 
The biggest limitation that exists for other tools (and some of them included in this repo) is that they do not
necessarily support edge/node labels and that they may not support visualizing 
[multigraphs](https://en.wikipedia.org/wiki/Multigraph) well. 