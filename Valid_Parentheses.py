class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Creamos una lista vacía en donde se va a almacenar el primer valor de s
        list = []
        # Iteramos sobre s
        for i in s:
            if i in "([{": # SI i es igual a alguno de estos valores
                list.append(i) # Agregar i a la lista list[]
            else: # De lo contrario, si i es un valor de cierre y el valor anterior es su equivalente de apertura
                if not list or \
                (i == ')' and list[-1] != '(') or \
                (i == '}' and list[-1] != '{') or \
                (i == ']' and list[-1] != '['):
                    return False # Retorna verdadero
                list.pop() #Eliminamos el valor si no cumple 
        return not list # Si la lista está vacía, retorna Falso
            
# Instanciamos la clase
solution = Solution()
s = input("Ingrese los valores: ") # Dentro de la variable s, ingresamos los valores a evaluar
print(solution.isValid(s)) # Llamamos la función
