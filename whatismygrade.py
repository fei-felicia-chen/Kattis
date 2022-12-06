C1_GRADE = 77
C2_GRADE = 85
C3_GRADE = 89
C4_GRADE = 80
NP_GRADE = 85
ASSIGNMENTS_WEIGHT = 55

weighted_c1 = C1_GRADE*0.09
weighted_c2 = C2_GRADE*0.12
weighted_c3 = C3_GRADE*0.12
weighted_c4 = C4_GRADE*0.12

weighted_np_for_c1 = NP_GRADE*0.09
weighted_np_for_nonc1 = NP_GRADE*0.12

print("Final grade if C1 gets replaced = ", (ASSIGNMENTS_WEIGHT + weighted_np_for_c1 + weighted_c2 + weighted_c3 + weighted_c4))
print("Final grade if C4 gets replaced = ", (ASSIGNMENTS_WEIGHT + weighted_c1 + weighted_c2 + weighted_c3 + weighted_np_for_nonc1))
