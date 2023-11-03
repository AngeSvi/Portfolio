def add (lifeList):
    """ajoute une nouvelle tache à la liste"""
    
    task = input ("What is the task? > ")
    when = input ("When is it due by? > ")

    level = ["high", "medium", "low"]
    priority = " "
    while priority not in level :
        priority = input ("What is the priority? (high, medium, low) > ").lower()

    newItem = [task, when, priority]
    
    lifeList.append(newItem)
    print("Thanks, this task has been added. \n")
    return lifeList
    
def view() :
    """donne aperçu de la liste des choses à faire selon priorité"""
    
    priorityChosen = input("Which type of task do you want to see ? (priority) > ").lower()

    for row in lifeList : 
        if priorityChosen in row :
            prettyPrint(row)
        else :
            prettyPrint(lifeList)

def edit(lifeList):
    """permet de modifier un item de la liste"""
    print(lifeList)
    task = " "
    while task not in lifeList[0] :
        task = input("Which task do you want to modificate ? > ")             
    lifeList = removeElt(task)
    lifeList = add(lifeList)
        

def removeElt(task):
    """permet de supprimer une tache de la liste"""
    for row in lifeList :
        if row[0] == task :
            lifeList.remove(row)

    return lifeList
    

def prettyPrint (stg) :
    for row in lifeList :
        print(*row, sep= ", ")
    print(" ")


lifeList = []

answer = " "

print("🌟Life Organizer🌟 \n")
while answer != "quit" :
    
    movement = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ").lower()
    print("\n")
    
    if movement == "add" :
        lifeList = add (lifeList)
        
    elif movement == "view" : 
        view()
        
    elif movement == "edit" : 
        edit(lifeList)
        
    elif movement == "remove" :
        prettyPrint(lifeList)
        task = " "
        while task not in lifeList[0] :
            task = input("Which task do you want to remove ? > ")
        lifeList = removeElt(lifeList)
        
    else : 
        print ("Input error, please try again")
        continue

    f = open("calendar.txt", "w")
    f.write(str(lifeList))
    f.close()
    answer = input("Do you want to see the menu again or quit? > ").lower()

    