def compute_tuition_owed(credit_hours, district_code):
    if district_code == 'I':
        return credit_hours * 250
    elif district_code == 'O':
        return credit_hours * 550
    else:
        return None

def main():
    last_name = input("Enter student's last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I for In district, O for Out of district): ").upper()

    tuition_owed = compute_tuition_owed(credit_hours, district_code)
    
    if tuition_owed is None:
        print("Invalid district code. Please try again.")
    else:
        print(f"Student {last_name}'s tuition owed: ${tuition_owed:.2f}")

if __name__ == "__main__":
    main()

