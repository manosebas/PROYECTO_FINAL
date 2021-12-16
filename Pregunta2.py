import unittest
import random

def TestValue_results():
    
    #5 Unit tests
    
    objeto = RandomizedSet()
    
    assert objeto.insert(1) == True, "Should inserts 1 to the set and return true as 1 was inserted successfully."
    assert objeto.remove(2) == False, "Should returns false as 2 does not exist in the set."
    assert objeto.insert(2) == True, "Should insert 2 to the set, returns true. Set now contains [1,2]."    
    assert objeto.getRandom() == 1 or 2, "Should return either 1 or 2 randomly."    
    assert objeto.remove(1) == True, "Should remove 1 from the set, returns true. Set now contains [2]."    
    assert objeto.insert(2) == False, "2 was already in the set, so return false."    
    assert objeto.getRandom() == 2, "Since 2 is the only number in the set, getRandom() should always return 2."
    
    #Otro ejemplo
    
    objeto2 = RandomizedSet()
    
    assert objeto2.insert(3) == True, "Should return True. inserta el 3"
    assert objeto2.remove(3) == True, "Should return True. elimina el 3"
    assert objeto2.insert(1) == True, "Should return True. inserta el 1"
    assert objeto2.getRandom() == 1, "Should return 1. solo tiene 1 para elegir"
    assert objeto2.remove(5) == False, "Should return False. No hay un 5 para eliminar"
    assert objeto2.insert(4) == True, "Should return True. Inserta el 4"
    assert objeto2.getRandom() == 1 or 4, "Should return 1 o 4. Cualquiera de los dos"
    
    #Otro ejemplo
    
    objeto3 = RandomizedSet()  
    
    assert objeto3.insert(5) == True, "Should return True. inserta el 5"
    assert objeto3.remove(2) == False, "Should return False. No hay 2 para eliminar"
    assert objeto3.insert(5) == False, "Should return False. No inserta el 5 porque ya existe"
    assert objeto3.getRandom() == 5, "Should return 5. Solo tiene el 5 para elegir"
    assert objeto3.remove(5) == True, "Should return True. Elimina el 5"
    assert objeto3.insert(1) == True, "Should return True. Inserta el 1"
    assert objeto3.getRandom() == 1, "Should return 1. Como 1 es el unico numero en el set returna 1"
    
    #Otro ejemplo
    
    objeto4 = RandomizedSet()

    assert objeto4.remove(2) == False, "Should return False. No hay 2 para eliminar"
    assert objeto4.insert(0) == True, "Should return True. Inserta el 0"
    assert objeto4.insert(3) == True, "Should return True. Inserta el 3"
    assert objeto4.insert(6) == True, "Should return True. Inserta el 6"
    assert objeto4.remove(5) == False, "Should return False. No hay 5 para eliminar"
    assert objeto4.insert(0) == False, "Should return False. No inserta el 0 porque ya existe"
    assert objeto4.getRandom() == 0 or 3 or 6, "Should return 0 o 3 o 6. Cualquiera de los tres"
    
    #Otro ejemplo
    
    objeto5 = RandomizedSet()
    
    assert objeto5.insert(9) == True, "Should return True. Inserta el 9"
    assert objeto5.insert(8) == True, "Should return True. Inserta el 8"
    assert objeto5.insert(7) == True, "Should return True. Inserta el 7"
    assert objeto5.remove(9) == True, "Should return True. Elimina el 9"
    assert objeto5.remove(8) == True, "Should return True. Elimina el 8"
    assert objeto5.remove(7) == True, "Should return True. Elimina el 7"
    assert objeto5.getRandom() == None, "Should return None no hay nada que elegir"
    
    
class RandomizedSet:
    
    #funcion para inicializar 
    def __init__(self):
        
        self.arreglo = []
        self.arr = {}

    #funcion para insertar un numero con complejidad O(1)
    def insert(self, numero):
        
        if numero in self.arr:
            return False #bool para confirmar si el numero existe o no, si ya existe, false y no se vuelve a insertar
        
        self.arreglo.append(numero)
        self.arr[numero] = len(self.arreglo) - 1
        return True #bool para confirmar que se inserto el numero

    #funcion para eliminar un numero con complejidad O(1)
    def remove(self, numero):
        
        if numero not in self.arr:
            return False #bool para confirmar si el numero existe o no, si no existe obviamente false y no elimina nada.
        
        index = self.arr[numero]
        
        if index < len(self.arreglo) - 1:
            borra = self.arreglo.pop()
            self.arreglo[index] = borra 
            self.arr[borra] = index
            
        else:
            
            self.arreglo.pop()
            
        del self.arr[numero]
        
        return True #bool para confirmar que se elimino el numero

    #funcion para obtener un numero aleatorio con complejidad O(1)
    def getRandom(self):
        tamanio = len(self.arreglo)
        if tamanio == 0:
            return None #bool none en caso de que el set este vacio
        else:
            return self.arreglo[random.randint(0, tamanio - 1)] #Elige aleatoriamente entre los numeros en el set


if __name__ == "__main__": 
    
    TestValue_results()
    print("\nAll test cases passed\n")

objeto = RandomizedSet()

#Mismo ejemplo del ejercicio
print("EXAMPLE 1 DEL EJERCICIO: \n")

output1 = objeto.insert(1) #Inserts 1 to the set. Returns true as 1 was inserted successfully.
print("Insert(1) = ", objeto.arreglo, output1)

output2 = objeto.remove(2) # Returns false as 2 does not exist in the set.
print("Remove(2) = ", objeto.arreglo, output2)

output3 = objeto.insert(2) # Inserts 2 to the set, returns true. Set now contains [1,2].
print("Insert(2) = ", objeto.arreglo, output3)

output4 = objeto.getRandom() # getRandom() should return either 1 or 2 randomly.
print("GetRandom() = ", objeto.arreglo, output4)

output5 = objeto.remove(1) # Removes 1 from the set, returns true. Set now contains [2].
print("Remove(1) = ", objeto.arreglo, output5)

output6 = objeto.insert(2) # 2 was already in the set, so return false.
print("Insert(2) = ", objeto.arreglo, output6)

output7 = objeto.getRandom() # Since 2 is the only number in the set, getRandom() will always return 2.
print("GetRandom() = ", objeto.arreglo, output7)

print("\nResumen: [ null", output1, output2, output3, output4, output5, output6, output7,"]")



objeto2 = RandomizedSet()

#Otro ejemplo
print("\n\nEXAMPLE 2: \n")

output1 = objeto2.insert(3) #True. inserta el 3
print("Insert(3) = ", objeto2.arreglo, output1)

output2 = objeto2.remove(3) #True. elimina el 3 
print("Remove(3) = ", objeto2.arreglo, output2)

output3 = objeto2.insert(1) #True. inserta el 1
print("Insert(1) = ", objeto2.arreglo, output3)

output4 = objeto2.getRandom() #1. Solo tiene el 1 para elegir
print("GetRandom() = ", objeto2.arreglo, output4)

output5 = objeto2.remove(5) #False. No hay un 5 para eliminar
print("Remove(5) = ", objeto2.arreglo, output5)

output6 = objeto2.insert(4) #True. Inserta el 4
print("Insert(4) = ", objeto2.arreglo, output6)

output7 = objeto2.getRandom() #1 o 4. Cualquiera de los dos 
print("GetRandom() = ", objeto2.arreglo, output7)

print("\nResumen: [ null", output1, output2, output3, output4, output5, output6, output7,"]")



objeto3 = RandomizedSet()

#Otro ejemplo
print("\n\nEXAMPLE 3: \n")

output1 = objeto3.insert(5) #True. inserta el 5
print("Insert(5) = ", objeto3.arreglo, output1)

output2 = objeto3.remove(2) #False. No hay 2 para eliminar 
print("Remove(2) = ", objeto3.arreglo, output2)

output3 = objeto3.insert(5) #False. No inserta el 5 porque ya existe
print("Insert(5) = ", objeto3.arreglo, output3)

output4 = objeto3.getRandom() #5. Solo tiene el 5 para elegir
print("GetRandom() = ", objeto3.arreglo, output4)

output5 = objeto3.remove(5) #True. Elimina el 5
print("Remove(5) = ", objeto3.arreglo, output5)

output6 = objeto3.insert(1) #True. Inserta el 1
print("Insert(1) = ", objeto3.arreglo, output6)

output7 = objeto3.getRandom() #1. Como 1 es el unico numero en el set returna 1
print("GetRandom() = ", objeto3.arreglo, output7)

print("\nResumen: [ null", output1, output2, output3, output4, output5, output6, output7,"]")


objeto4 = RandomizedSet()

#Otro ejemplo
print("\n\nEXAMPLE 4: \n")

output1 = objeto4.remove(2) #False. No hay 2 para eliminar 
print("Remove(2) = ", objeto4.arreglo, output1)

output2 = objeto4.insert(0) #True. Inserta el 0
print("Insert(0) = ", objeto4.arreglo, output2)

output3 = objeto4.insert(3) #True. Inserta el 3
print("Insert(3) = ", objeto4.arreglo, output3)

output4 = objeto4.insert(6) #True. Inserta el 6
print("Insert(6) = ", objeto4.arreglo, output4)

output5 = objeto4.remove(5) #False. No hay 5 para eliminar
print("Remove(5) = ", objeto4.arreglo, output5)

output6 = objeto4.insert(0) #False. No inserta el 0 porque ya existe 
print("Insert(0) = ", objeto4.arreglo, output6)

output7 = objeto4.getRandom() #0 o 3 o 6. Cualquiera de los tres
print("GetRandom() = ", objeto4.arreglo, output7)

print("\nResumen: [ null", output1, output2, output3, output4, output5, output6, output7,"]")



objeto5 = RandomizedSet()

#Otro ejemplo
print("\n\nEXAMPLE 5: \n")

output1 = objeto5.insert(9) #True. Inserta el 9
print("Insert(9) = ", objeto5.arreglo, output1)

output2 = objeto5.insert(8) #True. Inserta el 8
print("Insert(8) = ", objeto5.arreglo, output2)

output3 = objeto5.insert(7) #True. Inserta el 7
print("Insert(7) = ", objeto5.arreglo, output3)

output4 = objeto5.remove(9) #True. Elimina el 9
print("Remove(9) = ", objeto5.arreglo, output4)

output5 = objeto5.remove(8) #True. Elimina el 8
print("Remove(8) = ", objeto5.arreglo, output5)

output6 = objeto5.remove(7) #True. Elimina el 7
print("Remove(7) = ", objeto5.arreglo, output6)

output7 = objeto5.getRandom() #None no hay nada que elegir
print("GetRandom() = ", objeto5.arreglo, output7)

print("\nResumen: [ null", output1, output2, output3, output4, output5, output6, output7,"]")