import unittest

def TestValue_results():
    
    #5 Unit tests
    
    obj = Pregunta1()
    
    a1 = 1
    b1 = 3
    c1 = 5
    arreglo1 = [-4,-2,2,4]
    assert obj.ordenarArregloCuadratico(arreglo1, a1, b1, c1) == [3, 9, 15, 33], "Should be equal to [3 9 15 33]"
    
    a2 = -1
    b2 = 3
    c2 = 5
    arreglo2 = [-4,-2,2,4]
    assert obj.ordenarArregloCuadratico(arreglo2, a2, b2, c2) == [-23, -5, 1, 7], "Should be equal to [-23 -5 1 7]"
 
    a3 = 3
    b3 = 2
    c3 = 1
    arreglo3 = [1,2,3,4]
    assert obj.ordenarArregloCuadratico(arreglo3, a3, b3, c3) == [6, 17, 34, 57], "Should be equal to [6 17 34 57]"

    a4 = -2
    b4 = 2
    c4 = 2
    arreglo4 = [-2,-2,2,2]
    assert obj.ordenarArregloCuadratico(arreglo4, a4, b4, c4) == [-10, -10, -2, -2], "Should be equal to [-10 -10 -2 -2]"

    a5 = 9
    b5 = 3
    c5 = 6
    arreglo5 = [-3,-1,2,5]
    assert obj.ordenarArregloCuadratico(arreglo5, a5, b5, c5) == [12, 48, 78, 246], "Should be equal to [12 48 78 246]"


class Pregunta1:
    
    def ordenarArregloCuadratico(self, nums, a, b, c):
        
        tamanio = len(nums)
        nuevoArr = [0 for i in range(tamanio)]
        inicio = 0
        final = tamanio - 1
        centro = 0
        
        if a >= 0:
            centro = final
            
        while inicio <= final:
            
            # Aplicamos funcion cuadratica a cada elemento = a*x*x + b*x + c
            
            inicioArreglo = a * nums[inicio] * nums[inicio] + b * nums[inicio] + c
            finalArreglo = a * nums[final] * nums[final] + b * nums[final] + c
            
            if a >= 0:
                if inicioArreglo >= finalArreglo:
                    nuevoArr[centro] = inicioArreglo
                    centro -= 1
                    inicio += 1
                else:
                    nuevoArr[centro] = finalArreglo
                    centro -= 1
                    final -= 1
            else:
                if inicioArreglo <= finalArreglo:
                    nuevoArr[centro] = inicioArreglo
                    centro += 1
                    inicio += 1
                else:
                    nuevoArr[centro] = finalArreglo
                    centro += 1
                    final -= 1
        #retorna el arreglo en orden            
        return nuevoArr
    
    
if __name__ == "__main__": 
    
    TestValue_results()
    print("\nAll test cases passed\n")
    
    obj = Pregunta1()
    
    #Primeros 2 ejemplos son los mismos del ejercicio
    print("\nArrays in sorted order:\n ")
    
    a1 = 1
    b1 = 3
    c1 = 5
    arreglo1 = [-4,-2,2,4]
    respuesta1 = obj.ordenarArregloCuadratico(arreglo1, a1, b1, c1)
    print("\nExample 1: \n")
    print("Input: ", arreglo1, ", a = ",a1, ", b = ",b1, ", c = ",c1,"\nOutput: ", respuesta1)
    
    
    a2 = -1
    b2 = 3
    c2 = 5
    arreglo2 = [-4,-2,2,4]
    respuesta2 = obj.ordenarArregloCuadratico(arreglo2, a2, b2, c2)
    print("\nExample 2: \n")
    print("Input: ", arreglo2, ", a = ",a2, ", b = ",b2, ", c = ",c2,"\nOutput: ", respuesta2)
    
    a3 = 3
    b3 = 2
    c3 = 1
    arreglo3 = [1,2,3,4]
    respuesta3 = obj.ordenarArregloCuadratico(arreglo3, a3, b3, c3)
    print("\nExample 3: \n")
    print("Input: ", arreglo3, ", a = ",a3, ", b = ",b3, ", c = ",c3,"\nOutput: ", respuesta3)
    
    a4 = -2
    b4 = 2
    c4 = 2
    arreglo4 = [-2,-2,2,2]
    respuesta4 = obj.ordenarArregloCuadratico(arreglo4, a4, b4, c4)
    print("\nExample 4: \n")
    print("Input: ", arreglo4, ", a = ",a4, ", b = ",b4, ", c = ",c4,"\nOutput: ", respuesta4) 
    
    a5 = 9
    b5 = 3
    c5 = 6
    arreglo5 = [-3,-1,2,5]
    respuesta5 = obj.ordenarArregloCuadratico(arreglo5, a5, b5, c5)
    print("\nExample 5: \n")
    print("Input: ", arreglo5, ", a = ",a5, ", b = ",b5, ", c = ",c5,"\nOutput: ", respuesta5)
