import argparse
import spacy
import os
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_sm')

def is_noun(token):
    return token.pos_ in ['NOUN', 'PROPN']

def get_verb_edges(doc):
    edges = []
    for token in nlp(doc):
        subj = None
        dobj = None
        for child in token.children:
            if child.dep_ == 'nsubj' and is_noun(child):
                subj = child
            elif child.dep_ == 'dobj' and is_noun(child):
                dobj = child
        if subj and dobj:
            edges.append([subj.text, dobj.text, token.text])
    return edges

def get_adjective_edges(doc):
    edges = []
    for chunk in nlp(doc).noun_chunks:
        for token in chunk:
            if not is_noun(token):
                continue
            no_children = True
            for child in token.children:
                if child.dep_ in ['amod', 'acl', 'compound']:
                    no_children = False
                    edges.append([child.text, token.text, f'_{child.dep_}'])
            edges.append([token.text, token.text, f'_idx'])
    return edges

def get_edges(doc):
    edges = get_adjective_edges(doc)
    edges.extend(get_verb_edges(doc))
    return edges

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    args = parser.parse_args()

    with open(args.input_path) as fin:
        with open(args.output_path, 'w') as fout:
            for line in fin:
                for edge in get_edges(line.strip().lower()):
                    fout.write(','.join(edge))
                    fout.write('\n')

if __name__ == '__main__':
    main()