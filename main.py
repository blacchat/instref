import csv 


class Instr: 
    def __init__(self, instr, opcode, valid64, valid32, fflags, op1, op2, op3, op4, tuptype, desc): 
        self.instr = instr 
        self.opcode = opcode 
        self.valid64 = valid64 
        self.valid32 = valid32 
        self.fflags = fflags
        self.op1 = op1 
        self.op2 = op2 
        self.op3 = op3
        self.op4 = op4
        self.tuptype = tuptype 
        self.desc = desc 
    def printme(self):
        print("===============================")
        print("\033[0;34mInstruction\033[0m: " + self.instr)
        print("\033[0;34mDescription\033[0m: " + self.desc) 
        print("\033[0;34mOpcode\033[0m: " + self.opcode) 
        print("\033[0;34m64-bit Mode Support\033[0m: " + self.valid64) 
        print("\033[0;34m32-bit/Legacy Support\033[0m: " + self.valid32) 
        print("\033[0;34mCPUID Feature Flags\033[0m: " + self.fflags) 
        print("\033[0;34mOperand 1\033[0m: " + self.op1) 
        print("\033[0;34mOperand 2\033[0m: " + self.op2) 
        print("\033[0;34mOperand 3\033[0m: " + self.op3) 
        print("\033[0;34mOperand 4\033[0m: " + self.op4)
        print("\033[0;34mTuple Type\033[0m: " + self.tuptype) 
def welcome(): 
    print("+=====>x86-64 cheatsheet<=====+")
    print("-------------------------------")
def main(): 
    welcome() 
    with open("x86.csv") as f:
        z = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        raw = [i for i in z]
    f.close()
    data = [Instr(i[0], i[1], i[2], i[3], i[5], i[6], i[7], i[8], i[9], i[10], i[11]) for i in raw]
    while True: 
        x = input("\033[1;92m>\033[0m ").split(" ")
        if x[0] == "search":
            found = [] 
            for i in data: 
                if x[1].upper() == i.instr.split(" ")[0]: 
                    found.append(i)
            print(str(len(found)) + " items found.")
            for i in found: 
                i.printme() 
        elif x[0] == "exit":
            print("Exiting...")
            exit()
        else: 
            pass 
main() 
