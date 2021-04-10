import check50

@check50.check()
def exists():
    """kubas.cpp exists"""
    check50.exists("kubas.cpp")

@check50.check(exists)
def compiles():
    """kubas.cpp compiles"""
    check50.run("g++ kubas.cpp -lcrypt -lcs50 -lm -o kubas").exit(0)

@check50.check(compiles)
def emma():
    """responds to number 3"""
    check50.run("./kubas").stdin("3").stdout("9").exit()

@check50.check(compiles)
def rodrigo():
    """responds to number 5"""
    check50.run("./kubas").stdin("5").stdout("125").exit()
