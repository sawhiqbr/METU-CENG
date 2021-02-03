#############################################
#           MUHAMMED SAFA KABAR             #
#               2448504                     #
#             CENG111-THE3                  #
#############################################

#####################################################################
#                                                                   #
#                          HELPER FUNCTIONS                         #
#                                                                   #
#####################################################################

tree = []
leaves = []

def fake_deepcopy(somenestedlist):  #This function is for deepcopying part_list, since keeping part_list the same is not mandatory I didn't use it in the solution
    if len(somenestedlist) == 0:
        return []
    elif type(somenestedlist[0]) != list:
        return somenestedlist[:]
    else:
        return [somenestedlist[0][:]] + fake_deepcopy(somenestedlist[1:])

def children(part): #returns a part's (which is in part_list) children 
    return [[x,y] for (x,y) in part[1:]]

def check(ch, leaves): #checks if a part's children are in the leaves list
    same = []
    leaves_name = [x for [x,y] in leaves]
    ch_name = [y for [x,y] in ch]
    for item_name in ch_name:
        if item_name in leaves_name:
            same.append([ch[ch_name.index(item_name)][0]] + leaves[leaves_name.index(item_name)])
    if ch_name == [y for [x,y,z] in same]:
        return True, same
    return False, []

def make_tree_like(part_list): #makes an intermediate list which contains parts from part list in a tree-like order,
#                               hence makes it easier to convert part_list to a tree
    global tree
    global leaves
    if len(part_list) == 1:
        return [[1, part_list[0][0], part_list[0][1]]]
    while len(leaves) != len(part_list):
        for part in part_list:
            if type(part[0]) == list or part in leaves:
                continue
            if type(part[-1]) != tuple and part not in leaves:
                leaves.append(part)
            else:
                ch = children(part)
                sameness, allchildren = check(ch, leaves)
                if sameness:
                    val = 0
                    for child in allchildren:
                        del part_list[part_list.index(part)][1]
                        val += child[0]*child[-1]
                        part_list[part_list.index(part)].append([child])
                    leaves.append([part[0], val])
                    part_list[part_list.index(part)][0] = [1, part[0], val]
                    tree.append(part_list[part_list.index(part)])
    return tree

def children_2(part):
    leaves = []
    for i in part[1:]:
        if len(i) == 1:
            leaves.append(i[0][1])
        else:
            leaves.append("justaholder")
    return leaves

def insert(part, nottree_rem): # inserts part to remaining part of the not tree (which is returned from make_tree_like)
    if len(nottree_rem) == 0:
        return part
    for i in nottree_rem:
        ch = children_2(i)
        for j in ch:
            if j == "justaholder":
                continue
            if part[0][1] == j:
                part[0][0] = nottree_rem[nottree_rem.index(i)][ch.index(j)+1][0][0]
                nottree_rem[nottree_rem.index(i)][ch.index(j)+1] = part
                return nottree_rem
def make_real_tree(nottree): # inserts part to remaining part of the not tree (which is returned from make_tree_like)
    if len(nottree) == 1:
        return nottree
    else:
        return make_real_tree(insert(nottree[0], nottree[1:]))

def actual_children(node): # returns children of a node
    return node[1:]

def gimme_da_leaves(tree):# returns leaves of a tree
    if len(tree) == 0:
        return []
    elif type(tree[0]) != list:
        return [(tree[0], tree[1])]
    elif len(tree) == 1:
        return (tree[0][0], tree[0][1])
    else:
        s_list = []
        val = tree[0][0]
        for child in actual_children(tree):
            child[0][0] *= val
            some_parts = gimme_da_leaves(child)
            if type(some_parts) == list:
                for i in some_parts:
                    s_list.append(i)
            else:
                s_list.append(some_parts)
        return s_list

#################################################################################
#                                                                               #
#            THE FUNCTIONS WE ARE EXPECTED TO WRITE ARE BELOW                   #
#                                                                               #
#################################################################################

def calculate_price(part_list):
    global tree
    global leaves
    holder_list = fake_deepcopy(part_list)
    not_yet_tree = make_tree_like(holder_list)
    #not_yet_tree = make_tree_like(part_list)
    final_tree = make_real_tree(not_yet_tree)[0]
    tree = []
    leaves = []
    if type(final_tree[0]) != list: return final_tree[2]
    return final_tree[0][2]

def required_parts(part_list):
    global tree
    global leaves
    holder_list = fake_deepcopy(part_list)
    not_yet_tree = make_tree_like(holder_list)
    #not_yet_tree = make_tree_like(part_list)
    final_tree = make_real_tree(not_yet_tree)[0]
    req_list =  gimme_da_leaves(final_tree)
    tree = []
    leaves = []
    return req_list

def stock_check(part_list, stock_list):
    shortage_list =[]
    req_parts = required_parts(part_list)
    req_names = [y for [x,y] in req_parts]
    stc_names = [y for (x,y) in stock_list]
    for i in req_names:
        if i not in stc_names:
            a = req_parts[req_names.index(i)]
            shortage_list.append((a[1], a[0]))
        elif i in stc_names:
            req_ind = req_names.index(i)
            stc_ind = stc_names.index(i)
            shortage = req_parts[req_ind][0] - stock_list[stc_ind][0]
            if shortage > 0:
                shortage_list.append((i, shortage))
    return shortage_list
