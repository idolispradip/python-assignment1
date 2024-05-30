def check_admission(math_marks, physics_marks, chemistry_marks):
    if (math_marks >= 60 and
        physics_marks >= 50 and
        chemistry_marks >= 40 and
        (math_marks + physics_marks + chemistry_marks) >= 200):
        return "Eligible for admission"
    else:
        return "Not eligible for admission"

math_marks = int(input("Enter marks in Mathematics: "))
physics_marks = int(input("Enter marks in Physics: "))
chemistry_marks = int(input("Enter marks in Chemistry: "))

result = check_admission(math_marks, physics_marks, chemistry_marks)

print(result)
