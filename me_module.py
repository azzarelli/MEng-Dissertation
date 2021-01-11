"""
Meta Ethics module - refer to Body of Research for elaboration on module function
    Handles: MR1 - (a) Ego, (b) Super Ego
             MD1 - Id, instantaneous choice

    Inputs: I - represents an individual
            C_sego - Predetermined decision interms of Super Ego made by I
            C_id   - Predetermined decision interms of Id made by I
            C_ego  - AHP method, set of assigned ratings for the moral-wrongdoing of each choice, constrained by 0 < C_ego[i] < 1
                     proximity condition of 0.1 between choices, if satsified highest rank is taken, if not C_sego's decision over-rules
    Output:
            C_me - Final choice given by Metaethics module
"""
import numpy as np


SET = {'METAETHICS':{'EGO':{'ch1':0.1, 'ch2':0.6, 'ch3':0.8, 'ch4':0.9}, 'SEGO':'ch3', 'ID':'ch3'}}

# I understand the redundancy with returning the input, though this exists as a form of premptive planning; in the case where further development should occur to C_id() and C_sego() functions
def C_id(SET):
    return SET
def C_sego(SET):
    return SET

def C_ego(choice_set): # choice_set = dict:{'ch1':rank1, 'ch2':rank2,...,'chN':rankN}, where chX represent the choice ID and rankX is the associated rank
    c_set = np.clip([*choice_set.values()], 0,1) # unpack dict values and satisfy 0 < choice[i] < 1
    c_top, c_sec,  = [], []
    max_score = c_set.max() # max score to determine top choice(s)
    for c in choice_set:
        if choice_set[c] == max_score: c_top.append(c) # best choices, there maybe more than one
        elif choice_set[c] >= max_score-0.1: c_sec.append(c) # condition of proximity, append choices that do not satisfy (if there exist any)
    if c_sec or len(c_top) > 1: # if condition of proximity is not satsified or there are multiple top choices, need to incorporate comparison to superEgo
        return c_top + c_sec # form set of appropriate choices made by ego
    return c_sec # otherwise return the singular top choice

def meta_get(SET): # return choice made by metaethics
    c_id,c_ego,c_sego = C_id(SET['ID']),C_ego(SET['EGO']),C_sego(SET['SEGO'])
    if c_sego in c_ego: # ego condition 
        return c_sego
    else: # otherwise return id
        return c_id
    
# print(meta_get(SET['METAETHICS']))
