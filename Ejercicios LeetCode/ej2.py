def es_valida(s):
    dic = {')': '(', '}': '{', ']': '['}
    pila = []
    for x in s:
        if x in '({[':
            pila.append(x)
        else:
            if len(pila) == 0 or ( pila.pop() != dic.get(x) ):
                return False
    
    return len(pila) == 0

"""

"""
print(es_valida("()"))  
print(es_valida("()[]{}")) 
print(es_valida("(]")) 
