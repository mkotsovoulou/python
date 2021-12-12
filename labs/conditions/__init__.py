import check50
import check50.c

@check50.check()
def exists():
    """conditions.py exists."""
    check50.exists("conditions.py")

@check50.check(exists)
def correctInput():
    """Returns correct number of hastags """
    check50.run("python3 conditions.py").stdin("1").stdout("You will see 1 stars:").stdout("\n#\n").exit()
    check50.run("python3 conditions.py").stdin("2").stdout("You will see 2 stars:").stdout("\n#\n#\n").exit()
    
@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("python3 conditions.py").stdin("").reject()
    
@check50.check(exists)
def test_reject_charactery():
    """rejects a non-numeric height of "a" """
    check50.run("python3 conditions.py").stdin("a").reject()

@check50.check(exists)
def test_reject_wrongnumber():
    """rejects a invalid height of "5" """
    check50.run("python3 conditions.py").stdin("5").reject()
    check50.run("python3 conditions.py").stdin("0").reject()
    check50.run("python3 conditions.py").stdin("-1").reject()
    help = r"did you to chack for numbers < 1 or > 4?"
    
