import tkinter as tk
from tkinter import messagebox

# 1. SIMPLE DATA STORAGE
# Sirf zaroori data rakha hai
CANCER_INFO = {
   # Updated Data with 8 Cancer Types
CANCER_INFO = {
    "Breast Cancer": ["Lump in breast", "Change in size", "Nipple discharge", "Skin dimpling"],
    "Lung Cancer": ["Persistent cough", "Coughing blood", "Chest pain", "Shortness of breath"],
    "Skin Cancer": ["New mole", "Mole changing color", "Sore that wont heal", "Itchy patch"],
    "Colon Cancer": ["Blood in stool", "Change in bowel habits", "Abdominal pain", "Weight loss"],
    "Prostate Cancer": ["Difficulty urinating", "Frequent urination", "Blood in urine", "Pain in hips"],
    "Leukemia": ["Frequent infections", "Excessive fatigue", "Easy bruising", "Night sweats"],
    "Cervical Cancer": ["Unusual bleeding", "Pelvic pain", "Pain during intercourse", "Heavier periods"],
    "Liver Cancer": ["Yellow skin (Jaundice)", "Upper abdominal pain", "Loss of appetite", "Nausea"]
}

def analyze_risk():
    selected_cancer = cancer_var.get()
    symptoms = CANCER_INFO[selected_cancer]
    
    # Check karna kitne boxes tick hain
    score = 0
    for var in checkbox_vars:
        if var.get() == True:
            score += 1
            
    if score == 0:
        messagebox.showwarning("Warning", "Kam az kam ek symptom select karein!")
        return

    # Simple Risk Calculation
    total = len(symptoms)
    percentage = (score / total) * 100
    
    result_text = f"Result for {selected_cancer}:\n"
    result_text += f"Symptoms matched: {score} out of {total}\n\n"
    
    if percentage >= 75:
        result_text += "Risk Level: HIGH\nTask: Please visit a doctor immediately."
    elif percentage >= 50:
        result_text += "Risk Level: MEDIUM\nTask: Consult a medical professional soon."
    else:
        result_text += "Risk Level: LOW\nTask: Keep monitoring your health."
        
    messagebox.showinfo("Analysis Result", result_text)

def update_symptoms(*args):
    # Purane checkboxes khatam karna
    for widget in symptom_frame.winfo_children():
        widget.destroy()
    
    checkbox_vars.clear()
    
    # Naye checkboxes lagana
    selected = cancer_var.get()
    symptoms_list = CANCER_INFO[selected]
    
    for s in symptoms_list:
        var = tk.BooleanVar()
        checkbox_vars.append(var)
        cb = tk.Checkbutton(symptom_frame, text=s, variable=var, font=("Arial", 10))
        cb.pack(anchor="w", padx=10, pady=2)

# 2. MAIN WINDOW SETUP
root = tk.Tk()
root.title("Simple Cancer Symptom Checker")
root.geometry("400x500")

# Variables
cancer_var = tk.StringVar(value="Breast Cancer")
checkbox_vars = []

# UI ELEMENTS
lbl_title = tk.Label(root, text="Cancer Symptom Analyzer", font=("Arial", 16, "bold"), pady=10)
lbl_title.pack()

lbl_select = tk.Label(root, text="Select Cancer Type:")
lbl_select.pack()

# Dropdown menu
cancer_menu = tk.OptionMenu(root, cancer_var, *CANCER_INFO.keys(), command=update_symptoms)
cancer_menu.pack(pady=5)

# Frame for symptoms
lbl_instr = tk.Label(root, text="Select your symptoms:", font=("Arial", 10, "italic"))
lbl_instr.pack(pady=10)

symptom_frame = tk.Frame(root)
symptom_frame.pack(fill="both", expand=True)

# Analyze Button
btn_check = tk.Button(root, text="Check Risk Level", command=analyze_risk, 
                      bg="lightblue", font=("Arial", 11, "bold"), pady=5)
btn_check.pack(pady=20, fill="x", padx=50)

# Disclaimer
lbl_note = tk.Label(root, text="Note: This is for educational purposes only.", 
                    fg="red", font=("Arial", 8))
lbl_note.pack(side="bottom", pady=5)

# Initialize first list
update_symptoms()

root.mainloop()
