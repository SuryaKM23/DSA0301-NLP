import nltk
from nltk.sem.logic import LogicParser

# Create a logic parser
logic_parser = LogicParser()

# Define your first-order logic sentences as strings
sentence1 = "exists x. (cat(x) & black(x))"
sentence2 = "forall x. (dog(x) -> big(x))"

# Parse the sentences into first-order logic expressions
fol_expression1 = logic_parser.parse(sentence1)
fol_expression2 = logic_parser.parse(sentence2)

# Print the parsed expressions
print("Parsed FOL Expression 1:", fol_expression1)
print("Parsed FOL Expression 2:", fol_expression2)

# You can perform various operations on these expressions, such as simplification,
# inference, and more, depending on your specific requirements.
