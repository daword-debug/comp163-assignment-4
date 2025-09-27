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

study_options = ["Programming", "Math", "English", "History"]
user_choice = input("Choose what subject to study: ")

if user_choice in study_options:
    print(f"{user_choice} is a great option.")


    if user_choice == "Programming":
        print("Focus on studying zybooks.")
        if current_gpa < 3.0 or study_hours < 20:
            print("Try explaing code to someone to reinforce knowledge.")
        else:
            print("Consider advanced coding.")
    elif user_choice == "Math":
        print("Try taking notes, and solvng the problem without looking it up.")
        if current_gpa < 2.5 and stress_level > 60:
            print("Break assignments into smaller steps.")
        else:
            print("Challenge yourself with quizzes that are timed.")
    elif user_choice == "English":
        print("Read and try to comprehend before answering questions.")
        if study_hours > 30 or social_points < 30:
            print("Join a book club so you can understand a little better and get better socially.")
    elif user_choice == "History":
        print("Try to create timelines for the historical events.")
elif user_choice not in study_options:
    print(f"{user_choice} is not in the study options.")
else:
    print(f"{user_choice} is not valid")



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
   

print(f"Hello {student_name}, here are your starting stats: Gpa:{current_gpa}: Study hours:{study_hours} Social points:{social_points} Stress level:{stress_level}")

study_options = ["Programming", "Math", "English", "History"]
user_choice = input("Choose what subject to study: ")

if user_choice in study_options:
    print(f"{user_choice} is a great option.")


    if user_choice == "Programming":
        print("Focus on studying zybooks.")
    elif user_choice == "Math":
        print("Try taking notes, and solvng the problem without looking it up.")
    elif user_choice == "English":
        print("Read and try to comprehend before answering questions.")
    elif user_choice == "History":
        print("Try to create timelines for the historical events.")
        if current_gpa >= 3.5 and stress_level < 40:
            print("Use flashcards to stay up to date and retain information.")
elif user_choice not in study_options:
    print(f"{user_choice} is not in the study options.")
else:
    print(f"{user_choice} is not valid")

if (current_gpa < 2.5 or social_points < 50) and not (current_gpa < 2.5 and social_points < 50):
     print(f"consider tutoring to improve social skills or grades.")
elif current_gpa >= 2.5 and social_points >= 50:
    print("Keep up the good work!")
else:
    print("You may need academic or social help.")

final_check = input("Type Ready if you are ready")

if final_check == "Ready":
    print("i see you ready to play you think you ready for it")
else:
    print("Invalid ready check go back")

if (current_gpa >= 1.0):
    print("congrats you passed first level")
elif (current_gpa is not None):
    print("its time to give up")
if (current_gpa > 2.0) and (social_points > 20 ):
    print("You passed the 2nd Level only harder from here")
elif (current_gpa <= 2.0) or (study_hours < 20):
    print("You failed")

if (current_gpa > 3.5):
    print("Ok you might be a sweat")
elif (current_gpa <= 3.5) and (study_hours > 25):
    print("You alright ig")