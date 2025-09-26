# College Life Adventure Game  

## About the Game  
The **College Life Adventure Game** is a text-based simulation where you play as a student navigating a semester. Your choices about classes, studying, and social life affect your GPA, stress, and social points. The goal is to see how your balance (or lack of it) shapes your final outcome.  

---

## Branching Concepts Demonstrated  

This game was designed to showcase **Python branching and decision-making structures**:  

1. **If/Elif/Else Statements (Step 2: Course Load Decision)**  
   - Choosing Light, Standard, or Heavy course loads adjusts stats differently depending on GPA.  
   - Example:  
     - Low GPA with Light Load → More study hours, reduced stress.  
     - High GPA with Heavy Load → Manageable but stressful.  

2. **Comparison Operators (Step 2)**  
   - GPA thresholds (`<`, `>=`, etc.) determine stat adjustments.  

3. **Membership Operators (Step 3: Study Strategy)**  
   - Checks if chosen subject is valid (`in available_subjects`).  

4. **Logical Operators (Step 3)**  
   - Combining conditions (e.g., `(subject_choice == "Programming" and study_hours >= 25)`).  

5. **Identity Operators (Step 4: Final Assessment)**  
   - Uses `type(final_choice) is str` and `final_choice is not None`.  

6. **Nested If Statements (Step 4)**  
   - Multiple layered outcomes depending on GPA, study hours, and social points.  

---

## How to Run the Game  

1. Make sure you have **Python 3.x** installed.  
2. Save the game file as `college_life_game.py`.  
3. Open a terminal or command prompt and run:  
   ```bash
   python [username]_assignment_3.py
