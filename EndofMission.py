#call defs one by one btw some of them will show you output after first (run) ;
def decrypt_clue(text):
    mineo = ["and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif",
                "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
            "not", "or","pass","raise", "return", "True", "try", "while", "with", "yield","False"]
    #making list to put our words in
    bingo = []
    for word in range(len(mineo)):
        try:
            if mineo[word] in text:
                bingo.append(mineo[word])
        except:
            continue
    #i used this def to add final words in (finding [list]) for showing.
    return bingo
text ="ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutablesquantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversarblockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeertopeerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigitalsignaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnonfungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati"
moo =[]
moo = decrypt_clue(text)
for word in moo :
 x=[]
 x=print(word,text.count(word))
 #def count is for repeated word count.
     #now we want to separate True & False from the list of strings <<
 def solve_puzzles(puzzles):
    uwu = []
    for strx in puzzles:
        if strx:  # Checking if the string is not empty
            uwu.append(True)
        else:
            uwu.append(False)
    return uwu
co=[]
co = [1234, 0 , "", [], {}, 'False', '0', 'None', None, -1 , [1, 2, 3], {'key': 'value'}, True , '', '[]', '[1,2,3]', '{}', {'a':1}, 'True', 'ali', '1234', 1 , 0.1 , -0.1 , True , '' , '[]' , '[1,2,3]' , '{}' , {'a': 1} , 'True' , 'ali' , '1234' , 1 , True , '', '[]', '[1,2,3]', '{}', {'a':1}, 'True', 'ali','1234', 1 , 0.1 , -0.1]
uoa=[]
uoa = solve_puzzles(co)
print(uoa)
# puzzles = 1234,0,"",[],{},'False','0','None',None,-1,[1, 2, 3],{'key':'value'},True,'','[]','[1,2,3]','{}',{'a':1},'True','ali','1234',
      #  1,0.1,-0.1,True,'','[]','[1,2,3]','{}',{'a': 1},'True','ali','1234',1,True,'','[]','[1,2,3]','{}',{'a':1},'True','ali','1234',1,0.1,-0.1
  # (1 == True & 0 == False)
                       # After giving values ​​to the first function, press enter to display outputs (one by one) !!
import random
def calculate_magic_numbers(start,end):
    magic_nums = []
    for i in range(l):
        if i >= 0 and i <= end-start:
            m=random.randint(start,end)
            magic_nums.append(m)
    return magic_nums
start = int(input("Start with:"))
end = int(input("End with:"))
l = int(input("My range:"))
opx = calculate_magic_numbers(start,end)
print(opx)
print("tap to show next def results!<<")
import time 
def exam_numbers():
    valid_answer = 0 #number of correct and incorrect answers by user
    unvalid_answer = 0
    start_time = time.time() #start(operation)
    while time.time() - start_time < 20:
        binary_numbers = []
        for _ in range(4): #if we use(i,j,...) instead of (_) it would be useless cuz it wasnt used in command below.
         binary_numbers.append(random.choice("10"))
                                     #this function randomly displays 1,0 in 10 bits.
        decimal_numbers = list((int,input().split())) #map(function,iterable)
        for i in binary_numbers:
            for j in decimal_numbers:
                if j==int(i,2):               #two fors (binary =>> decimal)
                    valid_answer +=1
                else:
                    unvalid_answer +=1
        print(f"valid ans:{valid_answer}")
        print(f"unvalid ans:{unvalid_answer}")
        break
exam_numbers()
import string
def check_pass(users):
    for username,password in users:
        if len(password) >= 8 and any(ch.islower() for ch in password) and any(ch in string.punctuation for ch in password):
           print(f"{username} has this password:{password}!<3")
users = [("user1","DkPm@1234"),("user2","12345678"),("user3","34aJ@5678903"),("user4","98QQ7654378"),("user5","3866266DDnx@"),("user6","Q765pu4378")]
check_pass(users)
print("let pen show u latergi then <<tap>> to see last def!")
import turtle   #writing latergi(use Farsi) with import turtle<<
def r_f(t,sx,sz):
    t.right(sx)
    t.forward(sz)
def l_f(t,sx,sz):
    t.left(sx)
    t.forward(sz)
def latargi():
    xo = turtle.Screen()
    xox = turtle.Turtle()
    xox.shape("turtle")
    xox.pensize(5)
    xox.penup()
    xox.forward(180)
    xox.pendown()
    r_f(xox,90,100)
    r_f(xox,90,50)
    xox.bk(25)
    r_f(xox,90,80)
    r_f(xox,180,80)
    xox.right(90)
    xox.penup()
    xox.fd(63)
    xox.pendown()
    r_f(xox,90,50)
    xox.penup()
    xox.forward(15)
    xox.pendown()
    xox.circle(5)
    xox.penup()
    r_f(xox,90,5)
    r_f(xox,90,5)
    r_f(xox,90,46)
    xox.right(180)
    xox.pendown()
    xox.circle(5)
    xox.penup()
    xox.forward(40)
    r_f(xox,90,60)
    xox.pendown()
    r_f(xox,90,60)
    r_f(xox,270,55)
    r_f(xox,90,45)
    xox.penup()
    r_f(xox,90,50)
    xox.right(270)
    xox.pendown()
    xox.forward(50)
    xox.penup()
    r_f(xox,90,15)
    xox.pendown()
    xox.forward(10)
    r_f(xox,90,50)
    r_f(xox,90,26)
    xox.penup()
    xox.forward(26)
    r_f(xox,90,26)
    xox.right(180)
    xox.pendown()
    xox.circle(5)
    xox.penup()
    l_f(xox,90,27)
    xox.left(90)
    xox.pendown()
    xox.forward(40)
    l_f(xox,90,50)
    r_f(xox,90,70)
    r_f(xox,90,38)
    r_f(xox,90,18)
    xo.mainloop()
latargi()
def unlock_vault(clues):
    v=exam_numbers()
    pu=check_pass(users)
    clues=[]
    clues.append(moo[0])
    clues.append(uoa[0])
    clues.append(opx[0])
    clues.append(exam_numbers)
    clues.append(v)
    clues.append(check_pass)
    clues.append(pu)
    print(clues) #all the things we take from functions but (latengi)//screen.
result=[]
unlock_vault(result)
               #(THE END) </3
