def bad_idea():
    a = 10
    b = 10
    print(a is b)


    def bad_idea_2():
        c = 999
        d = 999
        print(c == d)


        if __name__=='__main__':
            bad_idea()
            bad_idea_2()
            