import check50

@check50.check()
def exists():
    """grit.cpp exists"""
    check50.exists("grit.cpp")

@check50.check(exists)
def compiles():
    """grit.cpp compiles"""
    check50.run("g++ grit.cpp -lcrypt -lcs50 -lm -o grit").exit(0)

@check50.check(compiles)
def emma():
    """responds to all 4s"""
    check50.run("./grit").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdout("4").exit()

@check50.check(compiles)
def emma():
    """responds to all 4s and last 3"""
    check50.run("./grit").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("4").stdin("3").stdout("3.9").exit()

@check50.check(compiles)
def rodrigo():
    """responds to all 3s and last 4"""
    check50.run("./grit").stdin("3").stdin("3").stdin("3").stdin("3").stdin("3").stdin("3").stdin("3").stdin("3").stdin("3").stdin("4").stdout("3.1").exit()