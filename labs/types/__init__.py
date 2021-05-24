import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """description""" # this is what you will see when running check50
    check50.exists("types.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def prints2():
    """prints "2?" """
    check50.run("python3 types.py").stdout("2\n", regex=True).exit(0)
