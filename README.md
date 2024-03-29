# Subset Sum Problem and Bit Distribution
The partition problem is an NP-Complete problem commonly found in the field of computer science, and engineering due to its use for task scheduling. Research has been conducted on heuristic and exact algorithms of the partition problems, as well as the particular instance hardness. The ratio of number of input set elements and the average number of bits to represent the input set has been found to have an effect on the instance hardness. In this paper this ratio is kept at a constant, in order to investigate how the bit distribution of the input set affects the hardness. The results show that the bit distribution affects instance hardness when evaluated with both, exact and heuristic algorithms.

Found in this repository is the source code used to generate and analyze the data for Nikita Sazhinov's bachelore degree project.

**How to run**

The driver code is contained within "record.py". Running that script will generate the templates and record the amount of recursions it took to complete the search with Branch & Bound algorithm for a certain instance. It will store the data in an excel document.

The "compare_algs.py" script similarly will generate excel sheets with data comparing heuristic algorithms and branch & bound.

Both of these scripts can be parametrized to adjust for your needs.
