from procon.myProCon.controller import ProCon

procon = ProCon.ProCon("FastaFiles\4503949.aligned", 0.1, 0.01, 0.05)
procon.inf_to_file("InfResult.txt")
procon.mut_to_file("MulResult.txt")
procon.tri_to_file("TriResult.txt")
procon.graph_to_file("GraphResult")
