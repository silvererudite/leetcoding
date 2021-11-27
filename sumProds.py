n = [-1,1,0,-3,3]
# n_copy = []
# prod = 1
# for i in range(len(n)):
#     for j in range(len(n)):
#         if i != j:
#             prod *= n[j]
#     n_copy.append(prod)
#     prod = 1
# print(n_copy)

def prodNums(n):
    prodsSoFar = 1
    prodsBefore = [0] * len(n)
    for i in range(len(n)):
        prodsBefore[i]  = prodsSoFar
        prodsSoFar *= n[i]
    afterProds = 1
    prodsAfter = [0] * len(n)
    for j in range(len(n)-1,-1,-1):
        prodsAfter[j] = afterProds * prodsBefore[j]
        afterProds *= n[j]

    # for i in range(len(prodsAfter)):
    #     prodsAfter[i] *= prodsBefore[i]
    return prodsAfter
print(prodNums(n))