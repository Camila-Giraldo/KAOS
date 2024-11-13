import tkinter as tk
import math

num = ""
oper = ""
dots = 1
operators = ["+", "-", "x", u"\u00F7"]
nums = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

def numer(x):
  global num, oper, dots, nums, operators
  allowed = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "x", u"\u00F7", ".", "(", ")"]
  z = screen.cget("text")
  y = list(z)
  ya = len(y)-1
  if y[ya] not in allowed:
    pass
  else:
      if x == "*" or x == "/":
        dots = 1
        if x == "*":
            y="x"
            num = num+y
            oper=oper+x
            screen.config(text=num)
        else:
            y= u"\u00F7"
            num = num+y
            oper=oper+x
            screen.config(text=num)
      else:  
          if x == "+" or x == "-":
              dots = 1
              num = num+x
              oper = oper+x
              screen.config(text=num)
              
          elif x == "(" or x == ")":
              if x == "(":
                  if y[ya] == "." or y[ya] in nums:
                      pass
                  else:
                      num = num+x
                      oper = oper+x
                      screen.config(text=num)
              elif x == ")":
                  if y[ya] == "." or y[ya] in operators:
                      pass
                  else:
                      num = num+x
                      oper = oper+x
                      screen.config(text=num)
              else:
                  num = num+x
                  oper = oper+x
                  screen.config(text=num)
          else:
                  num = num+x
                  oper = oper+x
                  screen.config(text=num)
              
          

def equal():
    global num, oper, dots
    x = eval(oper)
    num = str(x)
    screen.config(text=num)
    oper = num
    dots = 1
    z = list(num)
    for i in z:
        if i == ".":
            dots = 0

def DOT():
    global num, oper, dots
    permitido = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = screen.cget("text")
    x = list(num)
    xa = len(x)-1
    if x[xa] in permitido and dots == 1:
        num = num+"."
        oper = oper+"."
        screen.config(text=num)
        dots = 0

        

def clean():
    global num, oper, dots
    x = list(num)
    y=list(oper)
    xa = len(x)-1
    ya = len(y)-1
    if x[xa] == ".":
        dots = 1
    x.remove(x[xa])
    y.remove(y[ya])
    x = "".join(x)
    y = "".join(y)
    num=x
    oper = y
    if len(x) == 0:
        num = ""
        oper = ""
        screen.config(text="0")
    else:    
        screen.config(text=num)
    
    

def cleaner():
    global num, oper, dots
    num = ""
    oper = ""
    screen.config(text="0")
    dots = 1

def pi():
    global num, oper, dots
    if dots == 1:
        dots = 0
        num = num + "3.1415926"
        oper = oper+ "3.1415926"
        screen.config(text=num)

def sin():
    global num, oper
    x = float(eval(oper))
    res = math.sin(math.radians(x))
    num = str(res)
    oper = num
    screen.config(text=num)

def cos():
    global num, oper
    x = float(eval(oper))
    res = math.cos(math.radians(x))
    num = str(res)
    oper = num
    screen.config(text=num)

def tan():
    global num, oper
    x = float(eval(oper))
    res = math.tan(math.radians(x))
    num = str(res)
    oper = num
    screen.config(text=num)

def log():
    global num, oper
    x = float(eval(oper))
    res = math.log10(x)
    num = str(res)
    oper = num
    screen.config(text=num)

def exp():
    global num, oper
    x = float(eval(oper))
    res = math.exp(x)
    num = str(res)
    oper = num
    screen.config(text=num)

def backspace():
    global num, oper
    num = screen.cget("text")
    if num != "0":
        num = num[:-1]
        oper = num
        if len(num) == 0:
            num = "0"
        screen.config(text=num)

def factorial():
    num = screen.cget("text")
    

    if float(num).is_integer() == False:
        screen.config(text="Error")
    else:
        n = int(num)
        if n < 0:
            screen.config(text="Error")
        elif n == 0 or n == 1:
            screen.config(text="1")
        
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            screen.config(text=str(result))
        
root = tk.Tk()
root.resizable(False, False)
root.geometry("347x619+770+228")
root.title("Calculadora Científica")
root.configure(bg="#163020")

##########################screen############################

# Creación de la screen
screen = tk.Label(root, text="0", font=("Calibri", 25), bg="#F9E8D9", width=18, justify="right")
screen.place(x=20, y=20)

# Función para crear botones numéricos y operadores
def create_button(text, x, y, command, color):
    return tk.Button(root, text=text, bg=color, font=("Calibri", 13), width=10, command=command).place(x=x, y=y)

# Posiciones y comandos para los botones numéricos y operadores
button_positions = [

    ("CE", 10, 100, lambda: cleaner(), "#EE7214"),  # Color para borrar la entrada actual
    ("C", 120, 100, lambda: clean(), "#EE7214"),   # Color para borrar toda la operación
    ("⌫", 230, 100, backspace, "#EE7214"),         # Color para retroceder un carácter

    ("+", 230, 150, lambda: numer("+"), "#637E76"),  # Color para operación suma
    ("-", 230, 200, lambda: numer("-"), "#637E76"),  # Color para operación resta
    ("x", 230, 250, lambda: numer("*"), "#637E76"),  # Color para operación multiplicación
    ("/", 230, 300, lambda: numer("/"), "#637E76"),

    ("(", 10, 300, lambda: numer("("), "#637E76"),   # Color para paréntesis izquierdo
    (")", 120, 300, lambda: numer(")"), "#637E76"),  # Color para paréntesis derecho
    
    # Números
    ("1", 10, 350, lambda: numer("1"), "#F9E8D9"),
    ("2", 120, 350, lambda: numer("2"), "#F9E8D9"),
    ("3", 230, 350, lambda: numer("3"), "#F9E8D9"),
    ("4", 10, 400, lambda: numer("4"), "#F9E8D9"),
    ("5", 120, 400, lambda: numer("5"), "#F9E8D9"),
    ("6", 230, 400, lambda: numer("6"), "#F9E8D9"),
    ("7", 10, 450, lambda: numer("7"), "#F9E8D9"),
    ("8", 120, 450, lambda: numer("8"), "#F9E8D9"),
    ("9", 230, 450, lambda: numer("9"), "#F9E8D9"),

    ("0", 10, 500, lambda: numer("0"), "#F9E8D9"),  # Color para el número cero
    (".", 120, 500, lambda: DOT(), "#637E76"),      # Color para el punto decimal
    ("=", 230, 500, lambda: equal(), "#F9E8D9"),
    ("!", 230, 550, lambda: factorial(), "#F9E8D9"),    # Color para el botón de igual
    # ... Otros botones
]

# Creación de los botones numéricos y operadores
for text, x, y, command, color in button_positions:
    create_button(text, x, y, command, color)

# Posiciones y comandos para los botones científicos
scientific_button_positions = [
    ("SIN", 10, 150, sin, "#E75151"),
    ("COS", 120, 150, cos, "#E75151"),
    ("TAN", 10, 200, tan, "#E75151"),
    ("LOG", 120, 200, log, "#E75151"),
    ("EXP", 10, 250, exp, "#E75151"),    
    ("Π", 120, 250, lambda: pi(), "#E75151")
    # ... Otros botones científicos
]

# Creación de los botones científicos
for text, x, y, command, color in scientific_button_positions:
    create_button(text, x, y, command, color)


root.mainloop()
