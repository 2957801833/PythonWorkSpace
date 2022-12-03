def login(name,pwd,code):
    if name == "admin" and pwd == "123456" and code == "8888":
        print("Welcome")
    elif name != "admin" and pwd == "123456" and code =="8888":
        print("warning name")
    elif name == "admin" and pwd != "123456" and code =="8888":
        print("warning pwd")
    elif name == "admin" and pwd == "123456" and code != "8888":
        print("warning code")
    else:
        print("other warning ")