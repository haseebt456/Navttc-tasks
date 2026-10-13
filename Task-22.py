scores = [("Ali", 85), ("Ahmad", 92), ("Aisha", 78)]

def top_student(students):
    ### Code here
    maxim=0
    for item in students:
        if item[1] > maxim:
            maxim = item[1]
            topStudent = item[0]
    return topStudent
        
    pass

print(top_student(scores)) 