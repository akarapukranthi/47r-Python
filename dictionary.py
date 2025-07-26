#basic code of dictionary
details={
    "name":"kranthi",
    "age":25,
    "city":"hyderabad",
    "marks":90
}
print(details["name"])
print(details["age"])


#methods in dictionaries

#get()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
val=company.get("google")
print(val)

#keys()

ompany={
    "google":"sundar pichai",
    "apple":"tim cook",
}
val=company.keys()
print(val)


#values()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
val=company.values()
print(val)

#items()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
val=company.items()
print(val)

#update()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
company.update({"amazon":"jeff bezos"})
print(company)

#pop()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
company.pop("google")
print(company)

#pop item()

company={
    "google":"sundar pichai",
    "apple":"tim cook",
}
val=company.popitem()
print(val)


#sum of the elements and calculating the total marks of all students
marks={
    "bhagrav":100,
    "kranthi":78,
    "rakesh":108,
    "saketh":89,
    "devender":90
}
total=0
count=0
for i in marks:
  total+=marks[i]
  count+=1
print(total)
print(total/count)


#find the nested dicionary in an dictionary+
marks={
    "name":"kranthi",
    "batch":"47r",
    "profession":"student",
    "address": {
        "dno":67,
        "street":"kphb",
        "city":"hyderabad",
        "state":"telangana",
    }
}
print(marks["address"]["city"])


#find the max salary of an employee using dictionaries
emp={
    "raju":{"salaray":10000},
    "kranthi":{"salaray":20000},
    "rakesh":{"salaray":30000},
}
count=0
employee=""
for i in emp:
  if emp[i]["salaray"]>count:
    count=emp[i]["salaray"]
    employee=i
print(count,employee)


#print the maximum marks of an student
student={
    "name":"vikram",
    "marks":
     {"tel":36,"hin":45,"eng":67,"math":78,"sci":89,"soc":90}
}
sub=" "
high=0
for i in student:
   if i=="marks":
    for j in student[i]:
      if student[i][j]>high:
        high=student[i][j]
        sub=j
print(sub,high)




#print the name of the employee by using location ofcompany
emp={

    "companies":[{"name":"google","location":"north america"},{"name":"amazon","location":"south america"},
     {"name":"meta","location":"korea"},{"name":"microsoft","location":"north america"}]

}

company_list=[]
for i in emp["companies"]:
    for j in i:
        if i[j]=="google":
            company_list.append(i["location"])
print(company_list)
