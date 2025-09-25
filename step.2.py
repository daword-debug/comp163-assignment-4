student_name = "darin"
current_gpa = 3.1 
if current_gpa < 1.0:
    print("Gpa is too low")
elif 1.0 <= current_gpa <= 2.5:
    print(f"Current gpa is below average")
elif 2.5 <= current_gpa <= 3.5: 
    print("Good job, keep up the consistent work!")
elif 3.5 <= current_gpa <= 4.0:
    print("Excellent Job!")
else:
    print("Gpa is too high, 4.0 and below")
   
    

study_hours = 25
social_points = 20
stress_level = 50

if 0 <= stress_level <= 100:
    print(f"stress level is {stress_level}")
else:
    print(f"stress level should be between 0 and 100.")

print(f"Hello {student_name}, here are your starting stats: Gpa:{current_gpa}: Study hours:{study_hours} Social points:{social_points} Stress level:{stress_level}")