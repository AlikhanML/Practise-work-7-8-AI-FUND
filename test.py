p_high = 0.50  # Replace with your Task 1 probability.
p_low = 1 - p_high
actions = {
    'Extra': ([p_high, p_low], [0, -60]),
    'Usual': ([p_high, p_low], [-30, 0])
}
 
def EU(probs, utilities):
    return sum(p*u for p,u in
               zip(probs, utilities))
 
scores = {name: EU(*values)
          for name, values in actions.items()}
print(scores)
print(max(scores, key=scores.get))
