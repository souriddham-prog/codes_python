def fill(n):
    p=1
    mat=[]
    
    for i in range(n):
         ri=[]
         for j in range(n):
            if i%2==0:
             ri.append(p)
            else:
              ri.insert(0,p)
            p+=1
         mat.append(ri)
         
    for i in range (n):
       for j in range(n):
          print(mat[i][j],end="\t")
       print("\n")
    
 
def display(matrix):
   for i in range(0,len(matrix)):
      for j in range(0,len(matrix[0])):
         print(matrix[i][j],end='\t')
      print()

fill(5)

def matrix_waterImage(matrix):
   n=len(matrix)
   image=[]
   for i in range(0,n):
      image.append([])
      for j in range(0,n):
        image[i].append(matrix[n-1-i][j])
   return image

def matrix_rotation(matrix):
   n=len(matrix)
   new_matrix=[]
   for i in range(0,n):
      new_matrix.append([])
      for j in range(0,n):
         new_matrix[i].append(matrix[j][n-1-i])
   return new_matrix

def caller():
 size=int(input("Enter order of matrix:"))
 matrix=[]
 for i in range(0,size):
   matrix.append([])
   for j in range(0,size):
      matrix[i].append(int(input(f"Enter element for  ({i},{j}):")))

 print(matrix)
 print(matrix_waterImage(matrix))
 print(matrix_rotation(matrix))
   

def matrix_multiplication(premult_matrix,postmult_matrix):
   if len(premult_matrix[0])!=len(postmult_matrix):
      print("Multiplication not possible!!!")
      return
   new_matrix=[]
   for i in range(0,len(premult_matrix)):
      new_matrix.append([])
      for j in range(0,len(postmult_matrix[0])):
         temp=0
         for k in range(0,len(postmult_matrix)):
           temp+= premult_matrix[i][k]*postmult_matrix[k][j]
         new_matrix[i].append(temp) 
      
   return new_matrix

display(matrix_multiplication([[1,0],[0,3]],[[3,5],[5,8]]))