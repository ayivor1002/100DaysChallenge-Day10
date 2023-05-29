from art import logo

#add
def add(n1,n2):
  return n1+n2

#substract
def substract(n1,n2):
  return n1-n2

#multiply
def multiply(n1,n2):
  return n1*n2

#divide
def divide(n1,n2):
  return n1/n2


operations={
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide  
}

def calculator():
  print(logo)
  
  continuer=True

  num1= float(input("What's the first number?: "))
  
  for operation in operations:
    print(operation)
  
  while continuer:
    operation_symbol= input("Pick an operation from the line above: ")
    
    num2= float(input("What's the second number?: "))
    
    function=operations[operation_symbol]
    result=function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    
    should_continue=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    
    if should_continue=='n':
        continuer=False
        calculator()
  
    num1= result
 

calculator()