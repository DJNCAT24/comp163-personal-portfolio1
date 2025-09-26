student_name = "YourName"
current_gpa = 3.2
study_hours = 20
social_points = 50
stress_level = 35

# --- Step 1: Foundation: display welcome and starting stats (Test Case 1) ---
print(f"Welcome, {student_name}, to the College Life Adventure Game!")
print("Starting stats:")
print(f"  GPA: {current_gpa}")
print(f"  Study hours available this semester: {study_hours}")
print(f"  Social points: {social_points}")
print(f"  Stress level: {stress_level}")
print("-" * 50)

# --- Step 2: Course Planning Decision (if/elif/else + comparison ops) ---
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice (A/B/C): ").strip().upper()

if choice == "A":
    print("You chose Light course load.")
    if current_gpa < 2.5:
        study_hours += 10
        stress_level -= 5
        print("Low GPA -> extra study time allocated to recover.")
    elif current_gpa >= 3.5:
        social_points += 10
        stress_level -= 10
        print("High GPA -> you can safely socialize more.")
    else:
        study_hours += 5
        stress_level -= 3
        print("Moderate GPA -> modest adjustments made.")
elif choice == "B":
    print("You chose Standard course load.")
    if current_gpa >= 3.0 and current_gpa < 3.7:
        study_hours += 0
        stress_level += 5
        print("You maintain your balance but stress rises slightly.")
    elif current_gpa < 3.0:
        study_hours += 5
        stress_level += 8
        print("You need to study more to keep up with the standard load.")
    else:
        social_points += 5
        stress_level += 2
        print("You handle the load well; small social boost.")
elif choice == "C":
    print("You chose Heavy course load.")
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 15
        social_points -= 10
        print("High GPA allows you to take a heavy load, but it's stressful.")
    else:
        study_hours += 20
        stress_level += 25
        social_points -= 20
        print("Heavy load with lower GPA is risky — prepare for long hours.")
else:
    print("Invalid course load option chosen. No changes made.")
print("-" * 50)

# --- Step 3: Study Strategy Decision (membership + logical operators) ---
available_subjects = ["Programming", "Math", "English", "History"]
print("Choose a subject to focus on this semester:")
print("Options:", ", ".join(available_subjects))
subject_choice = input("Your subject choice: ").strip().title()

if subject_choice not in available_subjects:
    print("Invalid subject chosen. No study strategy applied.")
else:
    print(f"You chose to focus on {subject_choice}.")
    if (subject_choice == "Programming" and study_hours >= 25) or (current_gpa >= 3.0 and subject_choice == "Math"):
        current_gpa += 0.15
        social_points -= 5
        print("Your focused effort paid off academically, but you socialized less.")
    elif subject_choice == "English" or subject_choice == "History":
        current_gpa += 0.07
        if study_hours < 10:
            social_points += 8
            stress_level -= 3
            print("Less study time allowed more social activities.")
        else:
            social_points -= 2
            print("Study commitment reduced social time slightly.")
    else:
        current_gpa += 0.05
        print("Small improvement from extra focus.")
print("-" * 50)

# --- Step 4: Final Semester Assessment (use identity ops, nested ifs, multiple endings) ---
print("Final assessment time! Choose how you want to finish the semester:")
print("1) Prioritize grades")
print("2) Prioritize social life")
print("3) Balance both")
final_choice = input("Enter 1, 2, or 3: ").strip()

if final_choice not in ["1", "2", "3"]:
    ending = "Invalid final input - No Change"
else:
    if type(final_choice) is str and final_choice is not None:
        if final_choice == "1":
            if current_gpa >= 3.3:
                current_gpa += 0.2
                study_hours += 10
                stress_level += 10
                ending = "Dean's List"
            else:
                current_gpa += 0.1
                stress_level += 15
                ending = "Academic Push"
        elif final_choice == "2":
            if social_points >= 60 and stress_level < 70:
                social_points += 10
                current_gpa -= 0.1
                stress_level -= 10
                ending = "Party Animal"
            else:
                social_points += 5
                current_gpa -= 0.2
                stress_level -= 5
                ending = "Social Butterfly (with costs)"
        elif final_choice == "3":
            if study_hours >= 30 and social_points >= 40:
                current_gpa += 0.12
                social_points += 2
                stress_level += 2
                ending = "Well-Rounded Success"
            elif study_hours < 15 and social_points < 30:
                current_gpa -= 0.05
                social_points -= 5
                stress_level += 8
                ending = "Burnout Warning"
            else:
                current_gpa += 0.05
                social_points += 0
                stress_level += 0
                ending = "Balanced Semester"
    else:
        ending = "Invalid final input - No Change"

if current_gpa > 4.0:
    current_gpa = 4.0
if current_gpa < 0.0:
    current_gpa = 0.0
if stress_level > 100:
    stress_level = 100
if stress_level < 0:
    stress_level = 0

print("-" * 50)
print("Final results for", student_name)
print(f"  Final GPA: {current_gpa:.2f}")
print(f"  Final Study Hours: {study_hours}")
print(f"  Final Social Points: {social_points}")
print(f"  Final Stress Level: {stress_level}")
print(f"  Ending achieved: {ending}")

if ending == "Dean's List":
    print("Congrats! Your dedication led to top academic honors.")
elif ending == "Academic Push":
    print("You improved academically but at the cost of higher stress.")
elif ending == "Party Animal":
    print("Fun times! But watch for academic consequences.")
elif ending == "Social Butterfly (with costs)":
    print("You had a busy social semester; GPA suffered a bit.")
elif ending == "Well-Rounded Success":
    print("You managed a great balance between study and life.")
elif ending == "Burnout Warning":
    print("Danger! Reassess workload and self-care next semester.")
elif ending == "Balanced Semester":
    print("Steady outcomes; room to optimize next term.")
else:
    print("No clear outcome — consider making stronger choices next semester.")
