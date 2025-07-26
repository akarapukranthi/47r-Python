

# # rows=5
# # for i in range(1,rows+1):
# #     res = " "
# #     for j in range(1,rows+1):
# #         if j==rows or j==1 or i==(rows//2)+1:
# #             res += "*"+" "
# #         else:
# #             res+=" "+" "
# #     print(res)


# # rows=5
# # for i in range(1,rows+1):
# #     res = " "
# #     for j in range(1,rows+1):
# #         if i==1 or j==(rows//2)+1:
# #             res += "*"+" "
# #         else:
# #             res+=" "+" "
# #     print(res)


# # rows=5
# # for i in range(1,rows+1):
# #     res = " "
# #     for j in range(1,rows+1):
# #         if i==j or j==rows or j==1:
# #             res += "*"+" "
# #         else:
# #             res+=" "+" "
# #     print(res)



# # rows=5
# # for i in range(1,rows+1):
# #     res = " "
# #     for j in range(1,rows+1):
# #         if i==1 or i==rows or i+j==rows+1:
# #             res += "*"+" "
# #         else:
# #             res+=" "+" "
# #     print(res)

# rows=5
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,i+1):
#             res += "*"+" "
#     print(res)




# rows=5
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,i+1):
#             res += str(i)+" "
#     print(res)




# rows=4
# num=1
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,i+1):
#             res += str(num)+" "
#             num+=1
#     print(res)



# rows=4
# num=2
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,i+1):
#             res += str(num)+" "
#             num+=2
#     print(res)






# rows=4
# num=1
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,i+1):
#             res += str(num)+" "
#             num+=2
#     print(res)







# rows=5
# for row in range(rows):
#     res = " "
#     for col in range(row+1):
#             res += str(rows) + " "
#     rows= rows-1
#     print(res)





# rows=5
# for i in range(rows,0,-1):
#     res = " "
#     for j in range(1,i+1):
#             res += str(i)+" "
#     print(res)



rows=5
# for i in range(rows):
#     res = " "
#     for j in range(rows):
#       if (i< rows //2 and (i==j or j==rows-i-1)):
#             res = res + "*"+" "
#       else:
#            res = res + " "+" "
#     print(res)


# rows=5
# for i in range(rows):
#     res = " "
#     for j in range(rows):
#         if j==0 or j==rows-1 or (i==j and j<=rows//2) or  (i + j == rows- 1 and j >= rows // 2):
#             res += "*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# rows=5
# mid=(rows//2)+1
# for i in range(1,rows+1):
#     res = " "
#     for j in range(1,rows+1):
#         if i<=rows//2 and i==j or i+j==rows+1:
#             res = res + "*"+" "
#         else:
#             res = res + " "+" "
#     print(res)

# word="aabbccddeeff"
# i=0
# while i<len(word):
#   count=0
#   temp=" "
#   for j in range(1,len(word)-1):
#     if word[j+1]==word[j]:
#       temp+=word[j]
#       count+=1
#     else:
#       break

#   i+=count
# print(word[j],count)
 
rows=5
for i in range(1,rows+1):
    res = " "
    for j in range(1,rows+1):
        if j==rows or j==1:
            res += "*"+" "
        else:
            res+=" "+" "
    print(res)


# #patterns 
#     #       *
#     #      * *
#     #     *   *
#     #    *     *
#     #   * * * * *

rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)


#     #          *
#     #        * *
#     #      * * *
#     #    * * * *
#     #  * * * * * 
rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "+" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

    #  * * * * *
    #   * * * *
    #    * * *
    #     * *
    #      *

rows=5
for i in range(rows,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)


    #  * * * * *
    #    * * * *
    #      * * *
    #        * *
    #          *

rows=5
for i in range(rows,0,-1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "+" " 
    for j in range(1,i+1):
        res+="*"+" "
    print(res)


     #       *
     #      * *
     #     *   *
     #    *     *
     #   * * * * *

rows=5
for i in range(1,rows+1):
    res=" "
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        if i==j or i==rows or i==1 or j==1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)  


#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

rows=5
for i in range(1,rows):
    res=" "
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(rows,0,-1):
    res=" "
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)


#  * * * * * 
#   * * * *
#    * * *
#     * *
#      *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
rows=5
for i in range(rows,0,-1):
    res=" "
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(1,rows+1):
    res=" "
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)



