# -*- coding: utf-8 -*-
# @Time: 2019/10/10 9:43
# @Author: Edgar Qian
# @Email: qianneng_se@163.com
# @File: myProCon.py


from procon.myProCon.service import TripletFinder, MutualInformation, ProbabilityCalculator


class ProCon:
    def __init__(self, file, gap_percent=0.1, p_1=0.1, p_2=0.05):
        self.file = file
        self.gap_percent = gap_percent
        self.p_1 = p_1
        self.p_2 = p_2
        self.pc = ProbabilityCalculator.ProbabilityCalculator(file, gap_percent, p_1, p_2)
        self.mi = MutualInformation.MutualInformation(self.pc)
        self.tf = TripletFinder.TripletFinder(self.mi)

    def get_seq(self):
        return self.pc.get_seq()

    def get_seq_number(self):
        return self.pc.get_seq_number()

    def get_res_number(self):
        return self.pc.get_res_number()

    def get_inf(self):
        return self.pc.get_entropy_0()

    def get_gap_lst(self):
        return self.pc.get_gap_20()

    def get_probaa(self):
        return self.pc.get_probaa()

    def get_prob6aa(self):
        return self.pc.get_prob6aa()

    def get_freqaa(self):
        return self.pc.get_freqaa()

    def get_freq6aa(self):
        return self.pc.get_freq6aa()

    def get_mut_obj(self):
        return self.mi.get_mut_obj()

    def get_mut_inf(self):
        return self.mi.get_mut_inf()

    def get_triplets(self):
        return self.tf.get_triplets()

    def inf_to_file(self, filename):
        return self.pc.inf_to_file_20(filename)

    def mut_to_file(self, filename):
        return self.mi.mut_inf_to_file(filename)

    def tri_to_file(self, filename):
        return self.tf.tps_to_file(filename)

    def graph_to_file(self, filename):
        return self.tf.show_graph(filename)
