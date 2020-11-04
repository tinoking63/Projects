

def create_outline():
    """
    TODO: implement your code here
    """
    topics = [
    "* Introduction to Python",
    "* Tools of the Trade",
    "* How to make decisions",
    "* How to repeat code",
    "* How to structure data",
    "* Functions", 
    "* Modules"
    ]
    topics.sort()
    problems = [
        "Problem 1",
        "Problem 2",
        "Problem 3"
    ]
    print("Course Topics:")
    for item in topics:
        print(item)
    
    my_map = {}
    print("Problems:")
    for key in topics:
        my_map[key] = problems
        print(key,": " + ", ".join(my_map[key]))
    
    # topics = list(topics)
    grades = ("STARTED","GRADED","COMPLETED")

    S1 = ("1. ","Luke","Introduction to Python","Problem 2",grades[0])
    S2 = ("2. ","Corban","How to repeat code","Problem 1",grades[1])
    S3 = ("3. ","Faheemah","Tools of the Trade","Problem 3",grades[2])
    S = [S1, S2, S3]
    print("Student Progress:")
    S.sort(key=lambda i: i[4], reverse=True)
    for num, name, topic, problem, grade in S:
        print("{} {} - {} - {} [{}]".format(num, name, topic, problem, grade))
    pass


if __name__ == "__main__":
    create_outline()
