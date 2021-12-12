import check50
import check50.c

@check50.check()
def exists():
    """mario.py exists."""
    check50.exists("conditions.py")

@check50.check(exists)
def correctInput():
    """Returns correct number of hastags """
    check50.run("python3 conditions.py").stdin("1").stdout("You will see 1 stars:").stdout("\n#\n").exit()
    check50.run("python3 conditions.py").stdin("2").stdout("You will see 2 stars:").stdout("\n#\n#\n").exit()
    
@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("python3 conditions.py").stdin("").reject()
    
@check50.check(exists)   
def wrongInput():
    """Returns wrong input """
    from re import match
    
    expected = "[Ww]rong [Nn]umber\n"
    actual = check50.run("python3 conditions.py").stdin("5").stdout()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your print string?"
        raise check50.Mismatch("Wrong number (only between 1 and 4 are allowed)\n", actual, help=help)
