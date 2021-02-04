"""
RegExTractor
------------

Python regex generator.

Takes 2 or more strings (or even a single one) and generates a RegEx that
matches similar strings.
The generated RegEx always matches the original strings, but it also
generalizes, usually matching more.

"""

from subseq_tree import gen_tree, tree_to_regex, tree_to_HTML


def extract(strs):
    """ (The main function)
    Takes a list of strings and generates a RegEx that matches similar strings.
    """
    tree = gen_tree(strs)
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(tree)
    return tree_to_regex(tree)

def extract_HTML(strs):
    tree = gen_tree(strs)
    return tree_to_HTML(tree)


if __name__ == '__main__':
    s1 = 'SELECT * FROM PEOS'
    s2 = 'SELECT ALL FROM KAVLI'
    s3 = 'SELECT KATI FROM MOUNI'
    s4 = 'SELECT COLOUMN1234 FROM PINAKAS1235141'
    s5 = 'SELECT KUMNSSDFSFDFSDFSD_1 FROM HDFSIRUJJSAD_2'
    s6 = 'SELECT A_2B FROM TABLE_2A'
    s7 = 'SELECT A1_B FROM F_TABLE_4'
    
    print extract([s1, s2, s3,s4,s5])
    print

   # s1 = 'skull'
   # s2 = 'school'
   # print extract([s1, s2])
   # print

   # s1 = '<div></div>'
   # s2 = '<span></span>'
   # print extract([s1, s2])
   # print
