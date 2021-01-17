"""
Legal Influence module - refer to Body of Research for elaboration on module function
    Handles: LR1 - Normality Frame, how normal is the action that has been carried out
             LD1 - Inaction Frame, consequence due to inaction

    Inputs: NORM - set of votes that determine the normativity of a choice (in a legal perspective)
            INACTION - set of detriment weights for each choice
            SEVERITY - set of ranked choices in order of severity
            all sets of choices are in respective order of each other, i.e. choice ch1 = choice ch1 = choice s1
    Output:
            C_lw
"""
import random

SET = {'LAW':{'NORM':{'ch1':9, 'ch2':2, 'ch3':4, 'ch4':4, 'ch5':9}, 'INACTION':{'ch1':0.1, 'ch2':0.5, 'ch3':0.8, 'ch4':0.15, 'ch5':0.1}, 'SEVERITY':{'ch1':6, 'ch2':4, 'ch3':5, 'ch4':6, 'ch5':6}}}

def C_inaction(choice_set):
    weights = []
    sum_dc = sum(choice_set.values()) # sum of all choice detriments
    for d in choice_set:
        weights.append((2*choice_set[d]) - sum_dc) # equation for determining weights due to inaction W = 2Dc_n - Sum(all Dc)
                                            # looking for the largest negative weight, as it provides the largest detriment associated with all other possible choices
    ideal_pos = 0 # position of best weight in weights array
    other_vals = [] # if there are other choices with same weight
    for  i in range(len(weights)):
        if weights[i] < weights[ideal_pos]:
            ideal_pos = i
            other_vals = [] # reset other positions when a new ideal weight is found
        if weights[i] == weights[ideal_pos]: other_vals.append(i) # append equal detriment choices
    choice_list = list(choice_set) # concatinate for array callable by index (other_pos)
    choices = []
    for ov in other_vals:
        choices.append(choice_list[ov])
    return choices

def C_normative(choice_set):
    ideal_pos = 'ch1'
    other_pos = [] # other choices valued at same level
    for c in choice_set:
        if choice_set[c] > choice_set[ideal_pos]: # find the ideal choice, will have the largest value
            ideal_pos = c
            other_pos = []
        if choice_set[c] == choice_set[ideal_pos]: 
            other_pos.append(c) # append other choices with equivalent magnitude to ideal_pos
    return other_pos

def C_severity(choice_set, options):
    ideal_pos = 'ch1'
    other_pos = []
    for c in choice_set:
        if choice_set[c] > choice_set[ideal_pos]:
            ideal_pos = c
            other_pos = []
        if choice_set[c] == choice_set[ideal_pos]: 
            other_pos.append(c)
    if len(other_pos) == 1: return other_pos[0] # first we want to rank the severity and check if there aren't multiple competing (smal highest rank) choices
    else: # if there are multiple competing choices we can check if there are similarities to earlier choices from c_normative and c_inaction
        final_set = [] # the final choice set before return
        for o in options:
            if o in other_pos:
                final_set.append(o)
        if len(final_set) == 1 : return final_set[0] # if there is only one similar choice then return that
        elif len(final_set) > 0: return random.choice(final_set) # if there are more than one similarities randomly pick one, as at this stage the choices are valued as equivalent
        else: return random.chioce(other_pos)# if there are NO similarities return a random choice from the severity set
            
    
def law_get(SET): # return choice made by legal influence
    c_inaction = C_inaction(SET['INACTION'])
    c_normative = C_normative(SET['NORM'])
    print(c_inaction, c_normative)
    choices_sim = [] # array of choices present in c_inaction and c_normative
    for c in c_inaction:
        if c in c_normative:
            choices_sim.append(c)
    print(choices_sim)
    if len(choices_sim) == 1: return choices_sim[0]
    else:
        c_sev = C_severity(SET['SEVERITY'], choices_sim) # implement severity decider
        return c_sev

print(law_get(SET['LAW']))
