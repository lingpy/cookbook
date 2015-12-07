from lingpy import *
from lingpy.sequence.sound_classes import *
import networkx as nx
import html.parser
from L_similarity import local_score

data = csv2list('D_face.tsv')
taxa = [x[0] for x in data]
words = [''.join(x[1].split(' ')) for x in data]

def similarity_network(words, threshold):
    """
    Create a similarity network based on partial cognacy scores.
    """
    
    G = nx.Graph()
    m = Multiple(words)
    m.lib_align()

    # attach stuff to alignment
    alm = []

    for i,w1 in enumerate(words):
        alm += [[taxa[i],w1]]
        for j,w2 in enumerate(words):
            if i < j:
                d = local_score(w1, w2)

                n1 = '{0}'.format(i)
                n2 = '{0}'.format(j)
                if n1 not in G:
                    G.add_node(n1,
                            name=''.join(tokens2class(ipa2tokens(w1), 'sca')),
                            word=i
                            )
                if n2 not in G:
                    G.add_node(n2,
                        name=''.join(tokens2class(ipa2tokens(w2),'sca')), 
                        word=j
                        )
                
                if d <= threshold:
                    p = Pairwise(w1, w2)
                    p.align(mode='global')
                    almA = tuple(p.alignments[0][0])
                    almB = tuple(p.alignments[0][1])
                    p.align(mode='local')
                    locA = tuple(p.alignments[0][0])
                    locB = tuple(p.alignments[0][1])

                    if locA == almA and locB == almB:
                        eq = 'full'
                    else:
                        eq = 'half'

                    G.add_edge(n1, n2, distance=d, similarity=1-d,
                            etype=eq)
    
    return G, alm



g, alm = similarity_network(words, 0.3)
nx.write_gml(g, '.test.gml')
test = open('.test.gml').read()
with open('O_partial.gml', 'w') as f:
    f.write(html.parser.unescape(test))


