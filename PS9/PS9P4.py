def determine_pay_rate(job_code):
    if job_code == 'L':
        return 25
    elif job_code == 'A':
        return 30
    elif job_code == 'J':
        return 50
    else:
        return 0

def calculate_gross_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * pay_rate
    return gross_pay

def main():
    last_name = input("Enter employee's last name: ")
    job_code = input("Enter job code (L, A, or J): ").upper()
    hours_worked = float(input("Enter hours worked: "))

    pay_rate = determine_pay_rate(job_code)
    
    if pay_rate == 0:
        print("Invalid job code. Please try again.")
    else:
        gross_pay = calculate_gross_pay(hours_worked, pay_rate)
        print(f"Employee {last_name}'s gross pay: ${gross_pay:.2f}")

if __name__ == "__main__":
    main()
