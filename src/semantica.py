class Cuadruplo:
  def __init__(self, operation, arg1, arg2, res):
    self.operation = operation
    self.arg1 = arg1
    self.arg2 = arg2
    self.res = res

class Semantica:
  def __init__(self):
    self.cuadruplos = []

  def generarCuadruplo(self, op, arg1, arg2, res):
    if(arg1 == None and arg2 == None):
      cuadruplo = Cuadruplo(op, '', '', res)
      self.cuadruplos.append(cuadruplo)
    else:
      cuadruplo = Cuadruplo(op, arg1, arg2, res)
      self.cuadruplos.append(cuadruplo)

  def imprimirCuadruplos(self):
    cont = 1
    for i in self.cuadruplos:
      print(str(cont) + ') ' + str(i.operation) + ', ' + str(i.arg1) + ', ' + str(i.arg2) + ', ' + str(i.res))
      cont = cont + 1
    
  def intermediario(self, op, arg1, arg2, res):
    if op == 'print':
        self.generarCuadruplo('print', '' , '' , res)
    elif op == '=':
        self.generarCuadruplo('=', arg1, '', res)
    elif op == '||':
        self.generarCuadruplo('||', arg1, arg2, res)
    elif op == '&&':
        self.generarCuadruplo('&&', arg1, arg2, res)
    elif op == '<':
        self.generarCuadruplo('<', arg1, arg2, res)
    elif op == '>':
        self.generarCuadruplo('>', arg1, arg2, res)
    elif op == '==':
        self.generarCuadruplo('==', arg1, arg2, res)
    elif op == '!=':
        self.generarCuadruplo('!=', arg1, arg2, res)
    elif op == '+':
        self.generarCuadruplo('+', arg1, arg2, res)
    elif op == '-':
        self.generarCuadruplo('-', arg1, arg2, res)
    elif op == '*':
        self.generarCuadruplo('*', arg1, arg2, res)
    elif op == '/':
        self.generarCuadruplo('/', arg1, arg2, res)
    elif op == 'gotoF':
        self.generarCuadruplo('gotoF', arg1, '', res)
    elif op == "read":
        self.generarCuadruplo('read', '', '', res)
    elif op == "goto":
        self.generarCuadruplo('goto', '', '', res)
    elif op == "era":
        self.generarCuadruplo('era', '', '', res)
    elif op == "eraObjeto":
        self.generarCuadruplo('eraObjeto', '', '', res)
    elif op == "return":
        self.generarCuadruplo('return', '', '', res)
    elif op == "gosub":
        self.generarCuadruplo('gosub', '', '', res)
    elif op == "endfunc":
        self.generarCuadruplo('endfunc', '', '', '')
    elif op == "endProgram":
        self.generarCuadruplo('endProgram', '', '', '')
    elif op == "param":
        self.generarCuadruplo('param', arg1, '', res)
    elif op == "verifica":
        self.generarCuadruplo('verifica', arg1, arg2, res)