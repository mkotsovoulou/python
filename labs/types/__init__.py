import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """Is your file saved as types.py""" # this is what you will see when running check50
    check50.exists("types.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def prints2():
    """Does it print "2" when you input 1 for x and 1 for y ? """
    check50.run("python3 types.py").stdin(1).stdin(1).stdout("2.0\n").exit(0)
