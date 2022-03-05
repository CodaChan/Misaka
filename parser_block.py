# Copyright 2021 plainfebruary
# Completed on December 29, 2021

from ddparser import DDParser
import itertools
import time
import sys



# Cartesian product
def Cartesian(a, b):
    result = list(itertools.product(a, b))
    return result


# Parser：Corresponding to the semantic parsing algorithm
# based on syntactic dependencies in Section 3.2

def Parser(text):
    start = time.time()

    ld_set = []
    dp_set = []
    pv_set = []

    # Enable DDParser
    go = DDParser(use_pos=True)
    par_res = go.parse(text)[0]
    word, dep, dep_pos, postag = par_res['word'], par_res['deprel'], par_res['head'], par_res['postag']

    """
    print(word)
    print(dep)
    print(dep_pos)
    print(postag)
    """

    # Define all required variables

    v_set = []  # Verbs
    p_set = []  # Properties
    d_set = []  # Device
    l_set = []  # Location

    temp_set = []  ##Non-COO components of the command，who represent the set in dependencies

    # Extract all VOB relationships and find all entities
    for i in range(len(word)):
        temp_p = []
        temp_v = []
        if postag[i] == 'n' \
                and dep[i] == 'VOB':
            temp_p.append(i)
            temp_v.append(dep_pos[i]-1)


            for j in range(len(word)):
                if dep[j] == 'COO' and dep_pos[j] - 1 == i:
                    temp_p.append(j)

        if temp_p != []:
            p_set.append(temp_p)
            v_set.append(temp_v)

    for i in range(len(p_set)):
        for j in range(len(v_set)):
            if i == j:
                pv_set.append(Cartesian(p_set[i], v_set[j]))

    # Select "representative" elements from each entity set
    # for the next step of natural language parsing

    for i in range(len(p_set)):
        temp_set.append(p_set[i][0])

    # Dependent syntactic analysis of representative elements
    # Which means we find the Device for Properties

    for i in range(len(temp_set)):
        temp_d = []
        for j in range(len(word)):
            if postag[j] == 'n' and dep[j] == 'ATT' \
                    and dep_pos[j] - 1 == temp_set[i]:

                temp_d.append(j)

                for k in range(len(word)):
                    if dep[k] == 'COO' and dep_pos[k] - 1 == j:
                        temp_d.append(k)

        d_set.append(temp_d)

    # Generate "DP" semantic dependency triples

    for i in range(len(d_set)):
        for j in range(len(p_set)):
            if i == j:
                dp_set.append(Cartesian(d_set[i], p_set[j]))

    # Clean the temp_set for represent the device set

    temp_set = []

    # As same

    for i in range(len(d_set)):
        temp_set.append(d_set[i][0])

    # Dependent syntactic analysis of representative elements
    # Which means we find the Location for Device

    for i in range(len(temp_set)):
        temp_l = []
        for j in range(len(word)):
            if postag[j] == 'n' and dep[j] == 'ATT':
                point = dep_pos[j]

                if point - 1 == temp_set[i]:
                    temp_l.append(j)
                    for k in range(len(word)):
                        if dep[k] == 'COO' and dep_pos[k] - 1 == j:
                            temp_l.append(k)

                elif dep[point - 1] == 'ATT' and postag[point - 1] == 'f':
                    if dep_pos[point - 1] - 1 == temp_set[i]:
                        temp_l.append(j)
                        for k in range(len(word)):
                            if dep[k] == 'COO' and dep_pos[k] - 1 == j:
                                temp_l.append(k)

        l_set.append(temp_l)

    for i in range(len(l_set)):
        for j in range(len(d_set)):
            if i == j:
                ld_set.append(Cartesian(l_set[i], d_set[j]))
    """

    print(ld_set)
    print(dp_set)
    print(pv_set)
    """
    temp_1 = []
    for i in range(len(ld_set)):
        for j in range(len(ld_set[i])):
            for k in range(len(dp_set)):
                for l in range(len(dp_set[k])):
                    if i == k:
                        temp_1.append([ld_set[i][j][0],ld_set[i][j][1],dp_set[k][l][1]])
    # print("___________")
    temp_2 = []
    for i in range(len(pv_set)):
        for j in range(len(pv_set[i])):
            for k in range(len(temp_1)):
                if pv_set[i][j][0] == temp_1[k][2]:
                    temp_1[k].append(pv_set[i][j][1])


    # for i in range(len(temp_1)):
    #     print(word[temp_1[i][0]],'-',word[temp_1[i][1]],'-',word[temp_1[i][2]],'-',word[temp_1[i][3]])

    res_to_api = ""
    for i in range(len(temp_1)):
        res_to_api = res_to_api + word[temp_1[i][0]] + '-' + word[temp_1[i][1]] + '-' + word[temp_1[i][2]] + '-' + word[temp_1[i][3]] + ' '

    return res_to_api
    # print("___________")
    # end = time.time()
    # print('Cost',end - start,'s')

# 分别打开客厅和房间的台灯的电源，再打开大棚里的台灯的电源
if __name__ =="__main__":
    Parser(sys.argv[1])