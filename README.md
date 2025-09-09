# University Admission Procedure 🎓

This project simulates the admission process of a university with multiple departments.  
It reads applicants’ exam scores and priorities from a file, calculates their admission scores, and distributes them across departments based on their preferences and available seats.

---

## 📖 Project Overview
- Applicants apply with scores in Physics, Chemistry, Mathematics, Computer Science, and a special exam score.  
- Each applicant specifies three **priority departments** (e.g., Physics, Mathematics, Engineering).  
- Admission score is calculated based on the department:
  - **Physics** → average of Physics & Math  
  - **Chemistry** → Chemistry score  
  - **Mathematics** → Math score  
  - **Engineering** → average of Math & Computer Science  
  - **Biotech** → average of Physics & Chemistry  
- If the **special exam score** is higher than the calculated one, it is used instead.  
- Students are accepted in **three rounds**:
  1. First priority  
  2. Second priority  
  3. Third priority  
- Each department accepts up to `N` students (user-defined).  
- Results are written into text files for each department.

---

## 🛠️ Tech Stack
- **Python 3.x**
- Built-in libraries: `collections`, file I/O, sorting

---

## 📂 Input Format
Applicants’ data is read from a file named `applicants.txt`:


Example:
John Smith 85 90 78 88 92 Physics Engineering Mathematics
Alice Johnson 91 85 89 80 90 Mathematics Physics Chemistry



---

## ⚙️ Usage

### 1. Prepare `applicants.txt`
Put all applicants in the required format into the file `applicants.txt`.

### 2. Run the program
```bash
python main.py


When prompted, enter the number of students to accept per department:

3


Output

Results are saved into five separate text files:

biotech.txt

chemistry.txt

engineering.txt

mathematics.txt

physics.txt

Each file contains the list of accepted students for that department, sorted by:

Admission score (descending)

Name (alphabetical)

Example (physics.txt):

Alice Johnson 91.0
John Smith 89.5


🔄 Admission Algorithm

Round 1: Each student is considered for their first priority. If accepted, they are removed from further rounds.

Round 2: Remaining students are considered for their second priority.

Round 3: Remaining students are considered for their third priority.

Each round ensures that no department exceeds its quota (N).

📊 Example Run

Input (applicants.txt):

John Smith 85 90 78 88 92 Physics Engineering Mathematics
Alice Johnson 91 85 89 80 90 Mathematics Physics Chemistry
Bob Lee 70 75 80 85 88 Engineering Mathematics Physics


Console:

3
Biotech
Chemistry
Engineering
Mathematics
Physics


Output (physics.txt):

John Smith 92.0
Alice Johnson 91.0
