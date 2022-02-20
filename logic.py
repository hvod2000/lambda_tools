from lambdas import string_to_lambda_expression as l

FALSE = l("&&1")
TRUE = l("&&2")
AND = l("&&2!1!2")
OR = l("&&1!2!2")
CLASSIC_IF = l("&&&1!2!3")
POLISH_IF = l("&&&2!1!3")
LAZY_NOT = l("&&&2!1!3")
TRUNCATED_NOT = l(f"&({TRUE})!({FALSE})!1")
NOT = TRUNCATED_NOT
XOR = l(f"&&1!(1!{NOT})!2")
IMPLICATION = l(f"&&({TRUE})!2!1")
EQUIVALENCE = l(f"&&(2!{NOT})!2!1")
