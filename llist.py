from lambdas import string_to_lambda_expression as l
import ltuples
import logic

CONS = ltuples.PAIR
HEAD = ltuples.FIRST
TAIL = ltuples.SECOND
NIL = logic.FALSE
IS_NIL = l('&(&&2)!(&&&&&1)!1')
