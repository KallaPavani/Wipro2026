import re
EmpID="EMP123"  # o/p: email found
#EmpID="EMP12345" o/p: email not found bcoz the empid is followed by more than 3 digits
#1. re.match() → Check valid Employee ID (EMP followed by 3 digits)
#result=re.match(r"EMP\d{3}",EmpID)
#another method
result=re.match(r"^EMP\d{3}$",EmpID)
if result:
    print("Employee ID")
else:
    print("Employee ID not found")
#2. Uses re.search() to find the first occurrence of a valid email address in a given text
text="pavanikalla023@gmail.com"
#email_result=re.search(r"[\w\.-]+@[\w\.-]+.\w+",text)
email_result=re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}",text)
if email_result:
    print("Email address:",email_result.group())
else:
    print("Email not found")

# 3. Meta-characters and special sequences demonstration
sample_text="Joshith born on 25-03-2025"
# .  -> any character
# +  -> one or more
# *  -> zero or more
# ?  -> optional / non-greedy
# \w -> word characters
# \d -> digits
# \s -> whitespace

pattern=r"(\w+)\s+born\s+on\s+(\d{2}-\d{2}-\d{4})"
result=re.match(pattern,sample_text)
if result:
    print("Sample text:",result.group())
else:
    print("Sample not found")

# 4️. Capturing groups output
if result:
    print("\nMatchedgroups:")
    print("Full Sentence:",result.group(0))
    print("Name:",result.group(1))
    print("Date:",result.group(2))

else:
    print("Sample not found")


