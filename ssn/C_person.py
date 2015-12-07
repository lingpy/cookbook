from lingpy import *
import networkx as nx

data = csv2list('D_person.tsv')[1:]

words = [x[3] for x in data]
cogs = [x[4] for x in data]
grps = [x[-1] for x in data]
langs = [x[1] for x in data]

colors = {
        'Slavic' : 'blue',
        'Romance': 'red',
        'Germanic' : 'green'
        }

G = nx.Graph()
for i,w1 in enumerate(words):
    cls = ''.join(tokens2class(ipa2tokens(w1), 'sca'))
    G.add_node(
            'x_'+str(i),
            name=cls,
            color = colors[grps[i]],
            group = grps[i],
            lang = langs[i]
            )
    for j,w2 in enumerate(words):
        if i != j:
            pair = Pairwise(w1, w2)
            pair.align(distance=True, mode='local')
            d = pair.alignments[0][-1]
            clsA = ''.join(tokens2class(ipa2tokens(w1), 'sca'))
            clsB = ''.join(tokens2class(ipa2tokens(w2), 'sca'))
            if d < 0.5:
                G.add_edge(
                        'x_'+str(i),
                        'x_'+str(j),
                        distances = d
                        )

nx.write_gml(G, 'O_person.gml')
                    
