from typing import List, Dict
from model.sketch import Sketch
from math import pow

class Estimater:

    def estimate(self, sketchs: List[Sketch]) -> float:
        n = len(sketchs)
        if (n < 1):
            raise ValueError("")
        
        m = sketchs[0].m
        for i in range(1, n):
            if (sketchs[i].m != m):
                raise ValueError("")
            
        merged_ranks = [max([sketchs[i].ranks[j] for i in range(n)]) for j in range(m)]
        harmonic_mean = m/(sum([1/pow(2, merged_ranks[j]) for j in range(m)]))
        return self._get_correction_costant(m) * m * harmonic_mean
    
    def _get_correction_costant(self, m: int) -> float:
        return 0.7213 / (1 + 1.079/m)