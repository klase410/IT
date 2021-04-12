import check50

@check50.check()
def exists():
    """suma.cpp exists"""
    check50.exists("suma.cpp")

@check50.check(exists)
def compiles():
    """suma.cpp compiles"""
    check50.run("g++ suma.cpp -lcrypt -lcs50 -lm -o suma").exit(0)

@check50.check(compiles)
def emma():
    """responds to 2 + 5"""
    check50.run("./suma").stdin("2").stdin("5").stdout("7").exit()

@check50.check(compiles)
def rodrigo():
    """responds to 6 + 8"""
    check50.run("./suma").stdin("6").stdin("8").stdout("14").exit()
