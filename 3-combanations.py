from itertools import combinations

# Transaction database
transactions = [
    {'Milk', 'Bread', 'Butter'},
    {'Bread', 'Butter', 'Egg'},
    {'Milk', 'Bread', 'Egg'},
    {'Milk', 'Butter'},
    {'Bread', 'Butter', 'Egg'},
    {'Milk', 'Bread', 'Butter', 'Egg'}
]

# Minimum support and confidence
min_support = 0.3      # 30%
min_confidence = 0.4  # 40%

# Calculate support
def support(itemset):
    count = sum(1 for transaction in transactions if itemset.issubset(transaction))
    return count / len(transactions)

# Generate frequent 1-itemsets
items = set()
for transaction in transactions:
    items.update(transaction)

L1 = {}
for item in items:
    s = support({item})
    if s >= min_support:
        L1[frozenset([item])] = s

# Generate frequent 2-itemsets
L2 = {}
for pair in combinations(L1.keys(), 2):
    candidate = pair[0] | pair[1]
    s = support(candidate)
    if s >= min_support:
        L2[candidate] = s

# Generate frequent 3-itemsets
L3 = {}
for triple in combinations(L1.keys(), 3):
    candidate = triple[0] | triple[1] | triple[2]
    s = support(candidate)
    if s >= min_support:
        L3[candidate] = s

# Print frequent 3-itemsets
print("Frequent 3-itemsets:")
for itemset, sup in L3.items():
    print(set(itemset), "Support =", round(sup, 2))

# Generate association rules from 3-itemsets
print("\nAssociation Rules:")

for itemset, sup_itemset in L3.items():

    # 1 item -> 2 items
    for antecedent in combinations(itemset, 1):
        antecedent = frozenset(antecedent)
        consequent = itemset - antecedent

        conf = sup_itemset / support(antecedent)

        if conf >= min_confidence:
            print(
                f"{set(antecedent)} --> {set(consequent)} "
                f"(Support={sup_itemset:.2f}, Confidence={conf:.2f})"
            )

    # 2 items -> 1 item
    for antecedent in combinations(itemset, 2):
        antecedent = frozenset(antecedent)
        consequent = itemset - antecedent

        conf = sup_itemset / support(antecedent)

        if conf >= min_confidence:
            print(
                f"{set(antecedent)} --> {set(consequent)} "
                f"(Support={sup_itemset:.2f}, Confidence={conf:.2f})"
            )