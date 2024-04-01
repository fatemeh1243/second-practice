#now we want to separate True & False from the list of strings <<
def solve_puzzles(puzzles):
    uwu = []
    strx=(bool)
    for strx in puzzles:
        if strx:  # Checking if the string is not empty
            uwu.append(True)
        else:
            uwu.append(False)
    return uwu
co=[]
co = [1234, 0 , "", [], {}, 'False', '0', 'None', None, -1 , [1, 2, 3], {'key': 'value'}, True , '', '[]', '[1,2,3]', '{}', {'a':1}, 'True', 'ali', '1234', 1 , 0.1 , -0.1 , True , '' , '[]' , '[1,2,3]' , '{}' , {'a': 1} , 'True' , 'ali' , '1234' , 1 , True , '', '[]', '[1,2,3]', '{}', {'a':1}, 'True', 'ali','1234', 1 , 0.1 , -0.1]
uoa = solve_puzzles(co)
print(uoa)
# puzzles = 1234,0,"",[],{},'False','0','None',None,-1,[1, 2, 3],{'key':'value'},True,'','[]','[1,2,3]','{}',{'a':1},'True','ali','1234',
      #  1,0.1,-0.1,True,'','[]','[1,2,3]','{}',{'a': 1},'True','ali','1234',1,True,'','[]','[1,2,3]','{}',{'a':1},'True','ali','1234',1,0.1,-0.1
  # (1 == True & 0 == False)