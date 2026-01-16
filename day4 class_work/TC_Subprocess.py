import subprocess
result=subprocess.run(
    "echo Hii Pavani How r u",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)

subprocess.run(("python","TC_MultipleAbstract.py"))
subprocess.run(("python","TC_AbstractClass.py"))
#we can run other files in same file also using subprocess.run

#echo is a command here without echo keyword we cant get output
