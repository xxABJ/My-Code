PD = []

EN = 2

ien = 2

ns = False
pairs = False
pair = 0
while ien < 202:

    PD = sorted(PD)

    def np(x):

        print(f"\n Adding new prime   {x}   in PD...")
        PD.append(x)
        print(f"\nPD = {PD}\n")

    def start():

        print(f"\n=========================\nNext ien = {ien}\n and PD = {PD}\n")

    def en(x):

        d_ien = x

        print("Reaching the ending number when dividing by EN...\n")
        print(f"IEN = {x}\n")
        print("expression:")
        print(f"{d_ien} / {EN} = {d_ien  / EN}")

        print(f"\n{x}")

        loops = 0
        while True:

            loops += 1
            #d_ien = d_ien 
            # print(f"{d_ien} / {EN} = {d_ien  / EN}")
            new_d_ien = d_ien / EN
            print(f"{new_d_ien}")
            # print(str(new_d_ien).split('.')[-1][0])

            if str(new_d_ien).split('.')[-1][0] == '0':

                if new_d_ien > 2:

                    d_ien = new_d_ien
                    #input()
                    continue

                else:

                    print(f"\n *2* Ending number reached when dividing by EN = {d_ien}.\n")
                    return new_d_ien, loops

            else:

                print(f"\nEnding number reached when dividing by EN = {d_ien}.\n")
                return d_ien, loops

    def bPD(_bPD, EN):

        return _bPD * EN

    def shape_checker(x):
        """This is based on the BASE system and the so called 'shapes' assigned to each other number (odds for BASE10) to make up the required primes needed to make up that number.\n
        BASE10 primes are made of maybe principle shapes that have a 'tree' number that is uniquely there which is able to reach out to all of the remain numbers.\n
        0 1 2 3 4 5 6 7 8 9\n
        unique number = 7\n
        evolution of amounts of shapes increases when main numbers reaches the checkpoints.\n
        check points are in (1, 3, 5,) & (7, 9)\n
        Simply said, if numbers passes is 5 or below it can be made out of n amount of shapes.
        so a 4 can be made out of (is between 2 - 5 therefore n = 0 -> n+1 -> n=1), and due to evolution of this process, n now becomes 1, and if next number lands is a 7 or "8" or 9 (is between 6 - 9 therefore n already is 1 -> n+1 -> n=2), more simply that number can be made out of ATMOST 2 shapes (prime numbers).\n
        then if it was a 13 then n would be 3."""

        main_shape = x


        #brute force main shape
        ms_amount = 0
        for _ in range(1, main_shape, 1):

            if _ % 5 == 0:

                ms_amount += 1
                continue

            if _ % 10 == 0:

                ms_amount += 1
                continue


        #brute force sp
        main_shape_sp = int(main_shape / 2)

        ms_sp_amount = 0
        for _ in range(1, main_shape_sp, 1):

            if _ % 5 == 0:

                ms_sp_amount += 1
                continue

            if _ % 10 == 0:

                ms_sp_amount += 1
                continue

        if ms_sp_amount == 0:
            print(f"\nms_sp_amount = {ms_sp_amount} is set to 1.\nmain_shape_sp = int(main_shape / 2) = {main_shape_sp}\n")
            ms_sp_amount = 1


        print(f"ms_amount = {ms_amount} and ms_sp_amount = {ms_sp_amount}\n")


        ## key?
        if ms_amount == ms_sp_amount:

            print(f"\nmain shape = {main_shape} and main shape sp = {main_shape_sp} are the same.\n")
            print(f"WE DO NOT subtract EN from ien2.\n")
            return False


        elif ms_amount != ms_sp_amount:

            print(f"\nmain shape = {main_shape} is larger than main shape sp = {main_shape_sp}.\n")
            print(f"WE MAY need to subtract EN from ien2.\n")
            return True


    def divisible_from_PD(x):

        for _ in PD:

            if x % _ == 0 and x != _:

                print(f"\n{_} is a divisor of {x}.\n")
                return _

        print(f"\nNo divisors found for {x} in PD.\n")
        return False


    def divisible_by_7(x):

        d = x / 7
        if str(d).split('.')[-1][0] == '0':

                print(f"\n{x} is a multiple of 7.\n")
                return True

        print(f"\n{x} is not a multiple of 7.\n")
        return False



    # if ien in [2, 4, 8, 16, 32, 64]:

    #     input("ien in 2^n")
    #     continue

    primes = PD



    if primes == []:

        print("\nNo primes found yet.\nAdding Exceptional number (2).\n")
        np(2)

    # elif ien == 4:

    #     print("\nlogic later, 4 = (2, 2).\n")
    #     #continue

    # elif ien == 6:

    #     print("\nlogic later, 6 = (3, 3).\n")
    #     np(3)
    #     #continue

    else:

        start()

        _en, loops = en(ien)

        print(f"en = {_en}\n")


        if loops <= ien / 2 and ien == 4:

            print(f"Prime pairs are:\n  ( {_en} , {_en} ) = \n")
            if _en not in PD:
                np(int(_en))
            print(PD)
            input()
            ien += 2
            pairs = True
            pair = _en
            continue

        elif loops <= ien / 2 and _en != 2 and divisible_from_PD(_en) == False and ien - _en == _en:

            print(f"Prime pairs are:\n  ( {_en} , {_en} ) = \n")
            if _en not in PD:
                np(int(_en))
            print(PD)
            input()
            ien += 2
            pairs = True
            pair = _en
            continue

        else:

            #_en = _en[0]

            # if int(_en) != 2:
            #     if _en not in PD:
            #         np(int(_en))
            #     print(PD)


            #     _bPD = PD[-1]
            #     print(f"\nLast prime in PD = {_bPD}\n")

            #     print("expression: bPD * EN = f")
            #     print(f"{_bPD} / {EN} = {_bPD / EN}\n")
            #     f = bPD(_bPD, EN)
            #     print(f"f = {f}\n")


            if _en not in PD:
                np(int(_en))
            print(PD)

            dfpd = divisible_from_PD(_en)


            if dfpd != False and _en != dfpd:

                print(f"\n{_en} is divisible by {dfpd} in PD.\n")
                print(f"Therefore {_en} is not a prime number.\n")


                if _en in PD:
                    PD.remove(_en)
                    print(f"\n{_en} removed from PD.")

                print(f"PD = {PD}\n")

                print(f"old _en = {_en}  ,   we (dfpd = {dfpd}) * (_en/dfpd = {int(_en/dfpd)})\n")
                _en = dfpd * int(_en/dfpd)
                print(f"new _en = {_en}\n")

            
                input()


            _bPD = PD[-1]
            print(f"\nLast prime in PD = {_bPD}\n")


            if pairs == True:
                print(f"PAIR USED\npair = {pair} _bPD = {_bPD}")
                print("expression: pair * EN = f")
                print(f"{pair} * {EN} = {pair * EN}\n")
                f = pair * EN
                print(f"f = {f}\n")

            else:
                print("expression: bPD * EN = f")
                print(f"{_bPD} * {EN} = {_bPD * EN}\n")
                f = bPD(_bPD, EN)
                print(f"f = {f}\n")


            if (f - _en) % 2 == 0:

                print("-----------------------------------NEW STANDPOINT (sp) required?")
                print(f"sp = {f} = ien2")

                ien2 = f

                if int(ien2 / 2) % 2 != 0 and shape_checker(int(ien2)) == True:


                    print(f"\nold ien2 = {ien2}")

                    # ien2 - 2
                    # print(f"ien2 - EN = {ien2} - {EN} = {ien2 - EN}")

                    ien2 = ien2 - _en
                    print(f"ien2 - _en = {ien2 + _en} - {_en} = {ien2}")

                    print(f"new ien2 = {ien2}\n")


                    print(f"\nien2 = {ien2}\n")

                    print(f"{'-'*10}")
                    _en, loops = en(ien2)


                else:

                    print(f"\nien2 = {ien2}\n")


                    print(f"{'-'*10}")
                    _en, loops = en(ien2)

                    ## if _en not in PD: ??

                    if (f - _en) % 2 == 0:

                        input("EXTRA SP REQUIRED")
                        break

                ns = True



            if f - _en > ien:
                print(f"\n{f} - {_en} = {f - _en} > {ien}\nwe add new axiom?\n")
                _np = _bPD
                print(f"BIGGER\nNP1\nien{ien} - _np{_np} = {ien - _np}\n")
                np1 = ien - _np

            elif f - _en <= ien:
                np1 = f - _en
                print(f"SMALLER OR EQUAL\nNP1\n{f} - {_en} = {f - _en}\n")

            elif pairs == True and ns == False:
                print(f"NP1\nexpression:\nien - pair = {ien} - {pair} = {ien - pair}\n")
                np1 = ien - pair

            # else:
            #     np1 = f - _en
            #     print(f"NP1\n{f} - {_en} = {f - _en}\n")

            np2 = ien - np1
            print(f"NP2\n{ien} - {np1} = {ien - np1}\n")


            if (np1 == 1 and divisible_by_7(np2 + 1)) or (np2 == 1 and divisible_by_7(np1 + 1)): # incrementing by multiples of 7 - related to 7

                print(f"\n{np1} is not a prime number.\n")

                print(f"\n{f} - {_en} = {f - _en} -> + 1 = {f - _en + 1}\nwe add new axiom?\n")
                increment = int((f - _en + 1) / 7)
                print(f"Unique patter in drawing as well !\n Incrementing bPD by {increment} ((f - _en + 1) / 7) \n bPD ({_bPD})= {_bPD} + {increment} = {_bPD + increment}\n")
                print(f"NP1\nien - (_bPD + {increment}) = {ien} - {_bPD + increment} = {ien - (_bPD + increment)}\n")
                np1 = ien - (_bPD + increment)

                if np1 not in PD:
                    np(int(np1))

                np2 = ien - np1
                
                if np2 not in PD:
                    np(int(np2))



            if divisible_from_PD(np1) != False and np1 != divisible_from_PD(np1):

                d_np1 = divisible_from_PD(np1)

                print(f"\n{np1} is divisible by {d_np1} in PD.\n")
                print(f"Therefore {np1} is not a prime number.\n")

                print("trying to mirror mechanism of how we reuse 'PAIRS', but for the results ...")

                #print(f"old np1 = {ien - np2}  ,   we {divisible_from_PD(np2)} * {divisible_from_PD(np2)}\n")
                print(f"original np1 = (ien - _np) {np1}\nwe np1 ({np1}) / divisor ({d_np1})\n")
                np1 = int(np1 / int(d_np1))
                print(f"new np1 = {np1}\n")

                if np1 not in PD:
                    np(int(np1))

                np2 = ien - np1
                print(f"NP2\nien ({ien}) - np1 ({np1}) = {ien - np1}\n")

                if np2 not in PD:
                    np(int(np2))


            elif divisible_from_PD(np2) != False and np2 != divisible_from_PD(np2):

                d_np2 = divisible_from_PD(np2)

                print(f"\n{np2} is divisible by {d_np2} in PD.\n")
                print(f"Therefore {np2} is not a prime number.\n")

                print("trying to mirror mechanism of how we reuse 'PAIRS', but for the results ...")

                #print(f"old np2 = {ien - np1}  ,   we {divisible_from_PD(np1)} * {divisible_from_PD(np1)}\n")
                print(f"original np2 = {ien - np1}  ,   we f ({f}) - original np2 ({np2})\n")
                np1 = f - np2
                print(f"new np1 = {np1}\n")

                if np1 not in PD:
                    np(int(np1))

                np2 = ien - np1
                print(f"NP2\nien ({ien}) - np1 ({np1}) = {ien - np1}\n")

                if np2 not in PD:
                    np(int(np2))


            else:

                if np1 not in PD:
                    np(int(np1))

                if np2 not in PD:
                    np(int(np2))


    ns = False
    pairs = False
    input()
    ien += 2
    continue