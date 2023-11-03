class MidtermChatBot:
    def showSubjectName(self):
        print("AI for robot system")

    def showStudentYear(self, student_id):
        student_2_digit = int(str(student_id)[:2])
        year = 67-student_2_digit
        return year
        
    def calculator(self, operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2

    def main(self):
        while True:
            command = input()
            if command == 'subject':
                self.showSubjectName()
            elif command == 'year':
                student_id = input()
                year = self.showStudentYear(student_id)
                print(f"{year}")
            elif command == 'calc':
                operator = input()
                num1 = int(input())
                num2 = int(input())
                result = self.calculator(operator, num1, num2)
                print(f"{result}")

if __name__ == "__main__":
    chatbot = MidtermChatBot()
    chatbot.main()