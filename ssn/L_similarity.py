from lingpy import *

def local_score(a,b):
    """
    Define a local score in which gaps do not count in the normalization.
    """

    p = Pairwise(a,b)
    p.align(mode='local')
    
    simAB = p.alignments[0][-1]

    seqA = p.alignments[0][0]
    seqB = p.alignments[0][1]
    
    p = Pairwise(seqA,seqA)
    p.align()
    simA = p.alignments[0][-1]

    p = Pairwise(seqB,seqB)
    p.align()
    simB = p.alignments[0][-1]

    # check for a vowel in the alignment
    classes = tokens2class(seqA, 'cv')
    if 'V' in classes and len(seqA) >= 2:

        return 1 - ((2 * simAB)/(simA + simB))
    
    else:
        return 1
    

def normal_score(a,b):

    p = Pairwise(a,b)
    p.align(mode='local', distance=True)
    return p.alignments[0][-1]
