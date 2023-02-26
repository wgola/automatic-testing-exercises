class Hamming:
    @staticmethod
    def distance(genotype_a: str, genotype_b: str):
        if len(genotype_a) != len(genotype_b):
            Hamming.__raise_value_error(genotype_a, genotype_b)
        else:
            return Hamming.__count_hamming_distance(genotype_a, genotype_b)

    @staticmethod
    def __raise_value_error(genotype_a: str, genotype_b: str):
        len_a = len(genotype_a)
        len_b = len(genotype_b)
        message = "Genotyp {} jest dłuższy ({}) niż genotyp {} ({})"
        if len_a > len_b:
            raise ValueError(message.format("A", len_a, "B", len_b))
        else:
            raise ValueError(message.format("B", len_b, "A", len_a))

    @staticmethod
    def __count_hamming_distance(genotype_a, genotype_b):
        if genotype_a == genotype_b:
            return 0
        else:
            count = 0
            for gen_a, gen_b in zip(genotype_a, genotype_b):
                if gen_a != gen_b:
                    count += 1
            return count
