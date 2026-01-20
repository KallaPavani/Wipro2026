import re
text="HelloWorld"
result=re.match("Hii",text)
print(result)
result1=re.match("World",text)
print(result1)
#Why re.match("World", text) gives NO match
#re.match() ONLY checks the beginning of the string.If your pattern is not right at index 0 , it fails and returns none.
#Key rule: re.match() matches ONLY at the beginning of the string thats'why it gives o/p as no match found
if result1:
    print("match found")
else:
    print("no match found")

searchResult=re.search("Hello",text)
print(searchResult.group())
print(searchResult.start())
print(searchResult.end())


email="pavani023@gmail.com"
if re.match(r"[a-z,A-Z,0-9]+@",email):
    print("email found")
else:
    print("no email found")

result2=re.fullmatch(r"\d{10}","1234567898")
print(result2)

print(re.findall(r"\d+","50 and 100 and 200"))

for n in re.finditer(r"\d+","A1 B33 C444"):
    print(n.group(),n.start(),n.end())

for n in re.finditer(r"[a-z]","a0 b2 A1 B33 C444"):
    print(n.group(),n.start(),n.end())

for n in re.finditer(r"[A-Z]","a0 b2 A1 B33 C444"):
    print(n.group(),n.start(),n.end())

print(re.search(r"\d+","Age is 23"))

print(re.search(r"^a.*c$","alekhyac")) #o/p: match
#print(re.search(r"^a.*c$","clekhya")) o/p: does not match bcoz starting letter is not a and ending letter is not c

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

print(re.search("hello",text,re.I))
#re.I(ignorecase) is used to ignore the case for ex in text=Hello ,so when i did re.search("hello",text) it should print none but if we use re.I then it will ignore the case as long as its the same word

text2="one\ntwo\nthree\nfour\nfive"
print(re.findall(r"^[tf]\w+",text2,re.M))
