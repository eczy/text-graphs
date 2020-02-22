
import argparse
import networkx as nx
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    args = parser.parse_args()
    
    G = nx.DiGraph()

    with open(args.input_path) as fin:
        for line in fin:
            src, dst, edge = line.strip().split(',')
            if G.has_edge(src, dst):
                G[src][dst]['weight'] += 1
            G.add_edge(src, dst, type=edge, weight=1)

    plt.subplots(figsize=(10, 10))
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig(args.output_path)

if __name__ == '__main__':
    main()