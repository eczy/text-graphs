# Text Graphs
A simple example of graph generation from text.

We use the part-of-speech tagging and syntactic dependency parsing built into the `spaCy` library in order to extract nouns, adjectives, and verbs from a text corpus along with the relationships between them. We then use these relationships to generate a graph structure among nouns and adjectives where directed edges entail either a relation (verb) or a description (adjective, clausal modifier, compound noun).



# Example
To run this analysis on the provided sample text, run the following commands:
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python text_graph.py sample.txt sample_graph.csv
python viz.py sample_graph.csv sample_graph.png
```

You should now have a csv with source, destination, and edge type columns along with a graph similar to the following:

![Sample Graph Output](/img/sample.png)