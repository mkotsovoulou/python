import check50

@check50.check()
def exists():
    """readability.py exists."""
    check50.exists("grades.py")

@check50.check(exists)
def gradeA():
    """Returns A for grades between 90 and 100"""
    check50.run("python3 grades.py").stdin("90").stdout("A").exit(0)
    check50.run("python3 grades.py").stdin("100").stdout("A").exit(0)
    
@check50.check(exists)
def gradeB():
    """Returns B for grades between 80 and 89"""
    check50.run("python3 grades.py").stdin("80").stdout("B").exit(0)
    check50.run("python3 grades.py").stdin("89").stdout("B").exit(0)

@check50.check(exists)
def gradeC():
    """Returns C for grades between 70 and 79"""
    check50.run("python3 grades.py").stdin("80").stdout("C").exit(0)
    check50.run("python3 grades.py").stdin("89").stdout("C").exit(0)

@check50.check(exists)
def gradeD():
    """Returns D for grades between 60 and 69"""
    check50.run("python3 grades.py").stdin("60").stdout("D").exit(0)
    check50.run("python3 grades.py").stdin("69").stdout("D").exit(0)

@check50.check(exists)
def gradeF():
    """Returns F for grades between 60 and 69"""
    check50.run("python3 grades.py").stdin("0").stdout("F").exit(0)
    check50.run("python3 grades.py").stdin("59").stdout("F").exit(0)
    
def wrongNumber():
    """Returns wrong number"""
    check50.run("python3 grades.py").stdin("101").stdout("Wrong Grade").exit(0)
