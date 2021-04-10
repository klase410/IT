import check50

@check50.check()
def exists():
    """kvadratas.cpp exists"""
    check50.exists("kvadratas.cpp")

@check50.check(exists)
def compiles():
    """kvadratas.cpp compiles"""
    check50.run("g++ kvadratas.cpp -lcrypt -lcs50 -lm -o kvadratas").exit(0)

@check50.check(compiles)
def emma():
    """responds to number 2"""
    check50.run("./kvadratas").stdin("2").stdout("4").exit()

@check50.check(compiles)
def rodrigo():
    """responds to number 6"""
    check50.run("./kvadratas").stdin("6").stdout("36").exit()
