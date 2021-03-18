# Write a function to compute 5 / 0 and use try/ except to catch the exceptions

def compute():
    try:
        x = 5 / 0
    except:
        print("Error dividing by zero")

compute()
