def ask_yes_or_no(quetions: str) -> str :
    while True:
        ans = input(f"{quetions} YES/NO :").strip().lower()
        if ans in ("yes" "y"):
            return True
        if ans in ("no" "n"):
            return False
        print("Enter YES or NO :")

def ask_non_empty(questions: str) -> str :
    while True:
        ans = input(f"{questions} ").strip()
        if ans:
            return ans
        print("Can't be Empty :")

def ask_choices(questions : str , choices : list[str]) -> str :
    while True:
        print(questions)
        
        for i , a in enumerate(choices):
            i = 1
            print(f"{i}: {a}")
            
        ans = input("Enter choice:").strip().lower()
        if ans in choices:
            return ans 
        print(f"Enter one of these {choices} ")
        