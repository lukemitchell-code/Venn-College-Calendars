def main ():
    '''
    Brown_University = [1013,1126,1127,1128,1129,1130,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,214,215,216,217,321,322,323,324,325,326,327,328,329,]
    Cornell_University = (901,1011,1012,1013,1014,1126,1127,1128,1129,1130,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,122,1223,1224,1225,1226,1227,1228,1229,1230,1231,101,102,103,104,119,215,216,217,218,219,329,330,331,401,402,403,404,405,406,407,)

    i = 0
    while i < len(Brown_University):
        shared = False

        j = 0
        while j < len(Cornell_University):
            if Brown_University[i] == Cornell_University[j]:
                shared = True

                j = len(Cornell_University)

            j += 1

        if shared:
            print("Date {:901} is Shared".format(Brown_University[i]))
        else:
            print("Date {:901} is NOT Shared".format(Brown_University[i]))
        
        i += 1

    i = 0
    for i in Brown_University:
        shared = False

        j = 0
        for j in Cornell_University:
            if i == j:
                shared = True

        if shared:
            print("Date {:901} is Shared".format(i))
        else:
            print("Date {:901} is NOT Shared".format(i))
    
    '''
    print("\n\nGood bye \n\n")
    breakpoint = 0