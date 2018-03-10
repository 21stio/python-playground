def yo():
    def abc():
        print(__name__)

    print(abc.__module__)
    print(abc.__name__)

yo()