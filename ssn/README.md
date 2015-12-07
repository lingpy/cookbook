# Sequence Similarity Networks in LingPy

This repository describes two applications for the creation and exploration of sequence similarity networks in LingPy.

* an example for the detection of fused words (compounds)
* an example for the detection of borrowings

The files are named in such a way that they can easily be distinguished by their prefix:

* L-prefix stands for "library". These files contain code that is imported as a library by the example scripts.
* C-prefix stands for "code". These files are used to run the active code in the demonstration.
* D-prefix stands for "data". These files are used as input data for the code.
* O-prefix stands for "output". These files are produced by the code.

In order to run the detection of fused words, just type

```shell
$ python C_partial.py
```

In order to run the detection of borrowings just run:

```shell
$ python C_borrowings.py
```

If you want to run the code at once, use the make-file:

```shell
$ ./MAKE.sh
```

In both cases, GML-files will be produced as output. These files should be opened with software such as Cytoscape (http://cytoscape.org), to view the resulting network.

# Sources of the Data

* The dataset on partial cognate detection was taken from Hou (2003)
(http://bibliography.lingpy.org?key=Hou2003).  
* The dataset on borrowing
detection was taken from the IELex project (http://ielex.mpi.nl). 

In both cases, a small subselection of words was carried out.

# Results as Images

The results are given also as image-files in SVG format (files are prefixed by an I`_).

# Representation of Data

In order to have a less abundant labelling for the nodes, I have converted all data into sound classes and do take the sound-class string (using LingPy) to represent the nodes rather than the IPA transcription itself. For details on sound classes, please read List (2014, http://sequencecomparison.github.io). 
