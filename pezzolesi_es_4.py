class Calcolatrice:
    
   def __init__(self,num_1:int , num_2:int):
      self.num_1 = num_1
      self.num_2 = num_2
   
   @staticmethod
   def addizione(num_1,num_2):
         somma = num_1 + num_2
         return somma
   

   @staticmethod
   def sottrazione(num_1,num_2):
         differenza = num_1 - num_2
         return differenza

   @staticmethod
   def moltiplicazione(num_1,num_2):
         prodotto = num_1 * num_2
         return prodotto

   @staticmethod
   def divisione(num_1,num_2):
         if num_1 != 0:
            quoziente = num_1 / num_2
            return quoziente
         else:
            print("E' impossibile dividere per zero.")

print(Calcolatrice.addizione(10, 5))       
print(Calcolatrice.sottrazione(10, 5))    
print(Calcolatrice.moltiplicazione(10, 5)) 
print(Calcolatrice.divisione(10, 5))       








