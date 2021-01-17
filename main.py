import layers as lay



OPTIONS = int(input("Number of outcomes possible ? "))

PROBABILITY_OCC = []

while sum(PROBABILITY_OCC) != 1:
    PROBABILITY_OCC = list(map(float,input("Input an order of probabilities in the form 'a b c'").strip().split()))[:OPTIONS] 

print(PROBABILITY_OCC)
