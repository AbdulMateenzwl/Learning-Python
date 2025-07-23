class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    
    def examine_patient(self, patient):
        return f"Dr. {self.name} is examining {patient.name} for {patient.condition}"
    
    def prescribe_medicine(self, patient, medicine):
        return f"Dr. {self.name} prescribed {medicine} to {patient.name}"

class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition
    
    def visit_doctor(self, doctor):
        return f"{self.name} is visiting Dr. {doctor.name} ({doctor.specialization})"

class Hospital:
    def __init__(self, name):
        self.name = name
    
    def schedule_appointment(self, doctor, patient, time):
        return f"Appointment scheduled at {self.name}: {patient.name} with Dr. {doctor.name} at {time}"

doctor1 = Doctor("Ali", "Cardiology")
doctor2 = Doctor("Saqib", "Neurology")

patient1 = Patient("Mateen", 35, "chest pain")
patient2 = Patient("Waseem", 28, "headaches")

hospital = Hospital("City General Hospital")

print(patient1.visit_doctor(doctor1))
print(doctor1.examine_patient(patient1))
print(doctor1.prescribe_medicine(patient1, "Aspirin"))

print(hospital.schedule_appointment(doctor2, patient2, "2:00 PM"))

print(patient2.visit_doctor(doctor1))
print(doctor2.examine_patient(patient1))

del doctor1
print(patient1.visit_doctor(doctor2))
