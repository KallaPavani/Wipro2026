import re
# Strong Password Validation using Lookaheads (?=)

password = "Welcome1@3"

# Password rules using lookahead assertions
pattern = r"""
^
(?=.*[a-z])
(?=.*[A-Z])
(?=.*\d)
(?=.*[@#$%?&*])
[A-Za-z\d@#$%&*?]{8,}
$
"""

result=re.match(pattern,password,re.VERBOSE)  # re.VERBOSE allows comments and multi-line regex
if result:
    print("Strong password")
else:
    print("Weak password")

#Using Regex Modifiers
text="Hello\nworld\nPYTHON"

#Ex for ---- re.IGNORECase ----
match1 = re.search("python",text,re.I)
print("IGNORECase match:",match1.group() if match1 else "No match")

#Ex for ---- re.MULTILINE ----
match2 = re.findall(r"^world",text,re.MULTILINE)
print("MULTILINE matches:", match2)

#Ex for ---- re.DOTALL ----
match3 =  re.search(r"Hello.*PYTHON",text,re.DOTALL)
print("DOTALL match:", match3.group() if match3 else "No match")