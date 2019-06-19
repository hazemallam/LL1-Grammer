rulesList = []
terminals_and_nonTerminals = []
nullable_rules = []
nullable_nonTerminals = []
toBDW = []
bdw = []
bw = []
temport_for_processing = [] #for BW
first = []

first_of_right = []
deo = []
eo = []
fdb = []
fb = []
extend_fb = []
follow_set =  []
selection_set = []
def rules():

    number_of_rules  = int(input("how many rules ?"))
    for rule in range(number_of_rules):
        display_rule_number = input(str(rule + 1) + ": ")
        rulesList.append(display_rule_number)
    for rule in rulesList:
        symbols = rule.split("->")
        # print(symbols)
        left_hand_side = []
        left_hand_side.append(symbols[0])
        # print(left_hand_side)
        right_hand_side = []
        right_hand_side.append(symbols[1])
        left_hand_side.append(right_hand_side)
        terminals_and_nonTerminals.append(left_hand_side)
    print(terminals_and_nonTerminals)

# step 1 : find all nullable rules and nullable nonterminals
def nullableRules_and_nullableNonTerminals():

    ruleNumber = 1
    for symbol in terminals_and_nonTerminals:
        # print(symbol)
        if  '0' in symbol[1]:
            nullable_nonTerminals.append(symbol[0])
            nullable_rules.append(ruleNumber)
            print('nullable rule : ' + str(nullable_rules))
            print( 'nullable non terminal '+str(nullable_nonTerminals))
        ruleNumber += 1

#        search for another nullable rules and nullable terminals
#     for symbol in terminals_and_nonTerminals:
#         flag = 0
#         for RHS in symbol[1]:
#             for character in RHS:
#                 if character not in nullable_nonTerminals:
#                     flag = 1
#             if flag == 0:
#                 print(RHS[0])
#                 nullable_nonTerminals.append(RHS[0])
    for x in terminals_and_nonTerminals:
        if '0' not in x[1]:
            toBDW.append(x)
    print('tobdw' + str(toBDW))


#step 2 : compute the relation Begins Directly With for each nonterminal

def BDW():
    # ruleNumber = 1
    firstChar = 0
    for symbol in toBDW:
     # if firstChar not in nullable_nonTerminals:
     #    print('symbol' + str(symbol))
        for character in symbol[1]:
            # print(character)

            for singleChar in character:
                if singleChar not in nullable_nonTerminals:

                    temporal_list_for_bdw = []
                    temporal_list_for_bdw.append(symbol[0])
                    temporal_list_for_bdw.append(singleChar)
                    if temporal_list_for_bdw not in bdw:
                        bdw.append(temporal_list_for_bdw)
                    # print("bdw list" + str(bdw))

                    break
                else:
                    temporal_list_for_bdw = []
                    temporal_list_for_bdw.append(symbol[0])
                    temporal_list_for_bdw.append(singleChar)
                    if temporal_list_for_bdw not in bdw:
                        bdw.append(temporal_list_for_bdw)


        firstChar += 1
    print("bdw list" + str(bdw))
    for i in bdw:
        print(str(i[0]) , 'BDW',str(i[1]) )
    # print('bwd ' + str(bdw))

# step 3 : compute the relation Begins With

def BW():
    temporal_1 = []
    temporal_2 = []
    for symbol in bdw:
        temporal_list_for_bw = []
        temporal_list_for_bw.append(symbol[0])
        temporal_list_for_bw.append(symbol[1])
        if temporal_list_for_bw not in bw:
            bw.append(temporal_list_for_bw)
    # print('bw ' + str(bw)  )
    for symbol in bdw:
        temporal_1.append(symbol[0])
        temporal_2.append(symbol[1])
    for symbol in toBDW:
        if symbol[0] not in temport_for_processing:
            temport_for_processing.append(symbol[0])
        for n in symbol[1]:
            if n not in temport_for_processing and n not in  '0':
                temport_for_processing.append(n)
    flag = 0
    index = 0
    while flag == 0:
        flag = 1
        length = len(temporal_1)
        while (index < length):
            lis = [i for i, x in enumerate(temporal_1) if x == temporal_2[index]]
            for t in lis:
                write = []
                write.append(temporal_1[index])
                write.append(temporal_2[t])
                if write not in bw:
                    temporal_1.append(write[0])
                    temporal_2.append(write[1])
                    flag = 0
                    bw.append(write)
            index = index + 1

    for w in bdw:
        k = []
        k.append(w[0])
        k.append(w[0])
        if k not in bw:
            bw.append(k)
    for x in bdw:
        z = []
        z.append(x[1])
        z.append(x[1])
        if z not in bw:
            bw.append(z)



    print(' bw list' +str(bw))

    for i in bw:
        print(str(i[0]), ' BW ',str(i[1]) )
    # print('temporal for processing list '+ str(temport_for_processing))

# step 4 : compute the set of terminals First(x) for each symbol x in the grammar
def FIRST():

    for x in temport_for_processing:
        for z in x:
            a = []
            for w in bw:
                if z == w[0] and w[1].islower():
                    a.append(w[1])
            terminal = []
            terminal.append(z)
            terminal.append(a)
            if terminal not in first:
                first.append(terminal)

    print('first list' + str(first))

# Step 5. Compute First of right side of each rule

def FOR():
    temporal_for_FOR_processing = {}
    for b in first:
        temporal_for_FOR_processing[b[0]] = b[1]
    for a in toBDW:
        temporal = []
        for x in a[1]:
            # print(x)
            temporal.append(x)
            for charc in x:
                # print(charc)
                if not charc in nullable_nonTerminals:
                    if charc in temporal_for_FOR_processing:
                        transition = temporal_for_FOR_processing[charc]
                        for n in transition:
                            temporal.append(n)
                    break
                else:
                    if charc in temporal_for_FOR_processing:
                        transition = temporal_for_FOR_processing[charc]
                        for n in transition:
                            temporal.append(n)
            first_of_right.append(temporal)
    print('first of right ', str(first_of_right))

# Step 6. Compute the relation Is Followed Directly By

def FDB():
    for symbol in toBDW:
        for side in symbol[1]:
            for x in range(len(side)):
                # print(side[x])
                if side[0].isupper():
                    # print(side[x])
                    # break
                    if side[x] not in nullable_nonTerminals:
                        c = side[x].index(side[x])
                        # print(x)
                        # print(c)
                        a = []
                        if x != len(side) - 1:
                            a.append(side[x])
                        if x != len(side) - 1:
                            a.append(side[x + 1])
                        if a not in fdb:
                            fdb.append(a)
                    else:
                        a = []
                        if x != len(side) - 1:
                            a.append(side[x])
                        if x != len(side) - 1:
                            a.append(side[x + 1])
                        if a not in fdb:
                            fdb.append(a)

    print('follwed directly by ', str(fdb))
    fdb.pop(len(fdb)-1)
    for i in fdb:
        print(str(i[0]) , ' FDB ', str(i[1]))


# Step 7. Compute the relation Is Direct End Of

def DEO():
    for symbol in toBDW:
        for side in symbol[1]:
            # print(side)
            for index in reversed(range(len(side))):
                # print(side[index])
                if side[index] not in nullable_nonTerminals:
                    a = []
                    a.append(side[index])
                    a.append(symbol[0])
                    if a not in deo:
                        deo.append(a)
                    break
                else:
                    a = []
                    a.append(side[index])
                    a.append(symbol[0])
                    if  a not in deo:
                        deo.append(a)
    print('Direct end of list', str(deo))
    for i in deo:
        print(str(i[0]), ' DEO ', str(i[1]))

#     Step 8. Compute the relation Is End Of

def EO():
    for w in deo:
        k = []
        k.append(w[0])
        k.append(w[1])
        if k not in eo:
            eo.append(k)
    for x in deo:
        z = []
        z.append(x[0])
        z.append(x[0])
        if z not in eo:
            eo.append(z)

    for t in deo:
        r = []
        r.append(t[1])
        r.append(t[1])
        if r not in eo:
            eo.append(r)

    print('end of list ', str(eo))
    for i in eo:
        print(str(i[0]), ' EO ', str(i[1]))

#  Step 9. Compute the relation Is Followed By

def FB():
    for x in eo:
        for y in fdb:
            if x[1] == y[0]:
                for z in bw:
                    if y[1] ==z[0]:
                        a = []
                        a.append(x[0])
                        a.append(z[1])
                        if a not in fb:
                            fb.append(a)
    print('followed by ', str(fb))
    for i in fb:
        print(str(i[0]), ' FB ', str(i[1]))

# Step 10. Extend the FB relation to include endmarker

def EXTEND_FB():
    for symbol in eo:
        if symbol[0].isupper() and symbol[1] == 'S':
            a = []
            a.append(symbol[0])
            a.append('%')
            if a not in extend_fb:
                extend_fb.append(a)
    print('extend_fb ', str(extend_fb))
    for i in extend_fb:
        print(str(i[0]), ' FB ', str(i[1]))

# Step 11. Compute the Follow Set for each nullable nonterminal
def FOLLWO_SET():
    for symbol in fb:
        for i in range(nullable_nonTerminals.__len__()):
            if nullable_nonTerminals[i] == symbol[0] and symbol[1].islower():
                a = []
                a.append(nullable_nonTerminals)
                a.append(symbol[1])
                if a not in follow_set:
                    follow_set.append(a)

    print('follow set ', str(follow_set ) )

# Step 12. Compute the Selection Set for each rule


def SELECTIOIN_SET():
    # print(nullable_rules)
    # print(len(rulesList))
    for symbol in range(len(rulesList)):
        if isnullable(symbol+1):
            # length = len()
            a=[]
            a.append(follow_set[0][1])
            # a.append(follow_set[0][1])
            if a not in selection_set:
                selection_set.append(a)




        else:
            selection_set.append(first[symbol][1])
    print('selection list ' ,str(selection_set))




# check is nullable
def isnullable(index):
    for i in nullable_rules:
        if index == i:
            return  True
    return False
# nullable_nonTerminals = ['A','B']
# nullable_rules = [3,4]
# follow_set = [[['A'], 'c'], ['B'], ['c']]


class LL1Grammer:
    print('----------------------------working-------------------------------')
    rules()
    print('------------------------Step 1. Find all nullable rules and nullable nonterminals---------------------------------')
    nullableRules_and_nullableNonTerminals()
    print('------------------------Step 2. Compute the relation Begins Directly With for each nonterminal--------------------')
    BDW()
    print('------------------------Step 3. Compute the relation Begins With--------------------------------------------------')
    BW()
    print('------------------------Step 4. Compute the set of terminals First(x) for each symbol x in the grammar------------')
    FIRST()
    print('------------------------Step 5. Compute First of right side of each rule------------------------------------------')
    FOR()
    if len(nullable_nonTerminals)>0:
        print('--------------------Step 6. Compute the relation Is Followed Directly By--------------------------------------')
        FDB()
        print('--------------------Step 7. Compute the relation Is Direct End Of---------------------------------------------')
        DEO()
        print('--------------------Step 8. Compute the relation Is End Of----------------------------------------------------')
        EO()
        print('--------------------Step 9. Compute the relation Is Followed By-----------------------------------------------')
        FB()
        print('--------------------Step 10. Extend the FB relation to include endmarker--------------------------------------')
        EXTEND_FB()
        print('--------------------Step 11. Compute the Follow Set for each nullable nonterminal-----------------------------')
        FOLLWO_SET()
        # follow_set = [[['A'], 'c'], ['B'], ['c']]
    print('------------------------Step 12. Compute the Selection Set for each rule------------------------------------------')
    SELECTIOIN_SET()
    # print('Rules : '+str(rulesList))
    # print(temport_for_processing)