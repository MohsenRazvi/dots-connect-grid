from dots_connect import generate_populated_matrix,dot_connect


matrix,coords = generate_populated_matrix(30,30,30)
res = dot_connect(matrix,coords)
#pretty printing
for i in res:
    print(i)