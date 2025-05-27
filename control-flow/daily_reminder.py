task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to finish it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task, but it still needs to be done today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority level. Please enter high, medium, or low.")