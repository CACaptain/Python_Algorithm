
import unittest


large = 1000
string = "this should have been an int"
float = 1.0
broken_int = "this is a string"


assert large > 500
assert type(string)==type("")
assert type(float) != type(1)
assert type(broken_int) == type("")


