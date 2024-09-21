#Bank Details
class Bank:
    def __init__(self,bank_name,branch,name,acc_no,adhaar,balance):
        print("hello i am init function or constructor")
        self.bank_name = bank_name
        self.branch = branch
        self.name = name
        self.acc = acc_no
        self.ud = adhaar
        self.bal = balance

    def detail(self):
        print(f"""hello i am function
              Bank name = {self.bank_name}
              Branch = {self.branch }
              coustmer name = {self.name}
              Acc no = {self.acc}
              adhaar = {self.ud}
              balance = {self.bal }
              
              """)


s1 = Bank("sbi","chowk","vijay",24241342021, 122334456789,2000)

s1.detail()