# Patient Class is base for all following classes
class Patient():
# Appointment time
    time = ''

# initalising the __init__ constructor
    def __init__(self, name, age, apo_time, spec_doc, disease, **kwargs):
        self.name = name
        self.age = age
        self.apo_time = apo_time
        self.spec_doc = spec_doc
        # disease is a semi private element
        self._disease = disease
        Patient.time = apo_time
        print(f' chossen time for appointment by patient , {Patient.time}')

   # prints the appointment time of
    def appointment_time():
        print(f'The appointment time is {Patient.time}')
#creating a method using private data member
    def __patientDisease(self):
        print(f"The Patient is suffering from {self._disease}")

# Inheriting the Patient Class in Doctor()
class Doctor(Patient):
    # list to store data of doctors.
    doc_list = []

    def __init__(self, name, doc_id, doc_time, spec):
        self.name = name
        self.doc_id = doc_id
        self.doc_time = doc_time
        self.spec = spec
        Doctor.doc_list.append([self.name, self.spec, self.doc_time])

    def doc_details_lst(self):
        for doc_detail in Doctor.doc_list:
            print(doc_detail)

    def prescription(self):
        print("Go to medical shop")

    def fees_payment(self):
        print("Please pay the fees at counter")

class Med_Admi_Clerk(Doctor):
    def __init__(self):
        print("my self 'clerk', How can I Help you ?:")

    def book_apoint(self):
        doc_count = 0
        for item in Doctor.doc_list:
            if item[2] == Patient.time:
                doc_count += 1

        if doc_count >= 1:
            print(f'Appointment confirmed! Time is : {Patient.time}')

        else:
            print("your required time is not avialabe , please select other time")

# Implemented multiple Inhertence
class Nurse(Doctor,Patient):
    def __init__(self, patient_gender, patient_weight):
        print("Hii , I am nurse")
        self.patient_gender = patient_gender
        self.patient_weight = patient_weight

    def show_doc_details(self):
# we used super() to access the element from parent class
        for item in super().doc_list:
            print(item)

    def suggestions(self):
        print("Better chekc you weight", self.patient_weight)
# using a super() keyword to call method in parent class
        super().prescription()


class emergency():
    def __init__(self, emrgncy, gender):
        self.emrgncy = emrgncy
        self.gender = gender

    def join_emergency(self):
        print("the situation is worst?", self.emrgncy)
        print("the admit is ", self.gender)


doc1 = Doctor("Doctor1",11278,"morning","Cardiologists")
doc2 = Doctor("Doctor2",12234,"Noon","Neurologists ")
doc3 = Doctor("Doctor3",1234,"","Dermatologists.")
doc4 = Doctor("Doctor4",1234,"mor","Endocrinologists")

print("\n")
pat1 = Patient("Micker",28,"morning","lungs","Cancer")
pat1._Patient__patientDisease()


doc4.doc_details_lst()

clerk = Med_Admi_Clerk()
clerk.book_apoint()

nurse = Nurse("Nurseied",123)
nurse.show_doc_details()
nurse.suggestions()

