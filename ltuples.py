from lambdas import string_to_lambda_expression as l
from lambdas import reduce_lambda_to_beta_normal_form as b

PAIR = l("&&&2!3!1")
CLASSIC_FIRST = l("&(&&2)!1")
CLASSIC_SECOND = l("&(&&1)!1")
POLISH_FIRST, POLISH_SECOND = CLASSIC_SECOND, CLASSIC_FIRST
FIRST, SECOND = POLISH_FIRST, POLISH_SECOND

SHEME = l("&&1!2")
SHEME_BUILDER = l("&&&(&2!1!3)!3")
TUPLE_BUILDER = l("&(&1)!1")
T = {}
for i in range(64 + 1):
    T[i] = b(l(f"({SHEME})!{TUPLE_BUILDER}"))
    SHEME = b(l(f"({SHEME})!{SHEME_BUILDER}"))
