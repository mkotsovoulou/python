import check50

@check50.check()
def exists():
    """mario.py exists."""
    check50.exists("mario.py")

@check50.check(exists)
def correctInput():
    """Returns correct number of hastags """
    check50.run("python3 mario.py").stdin("1").stdout("#").exit()
    check50.run("python3 mario.py").stdin("2").stdout("##").exit()
    
    
@check50.check(exists)   
def wrongInput():
    """Returns wrong grade for invalid grades"""
    from re import match
    
    expected = "[Ww]rong [Nn]umber\n"
    actual = check50.run("python3 mario.py").stdin("5").stdout()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your print string?"
        raise check50.Mismatch("Wrong number (only between 1 and 4 are allowed)\n", actual, help=help)
