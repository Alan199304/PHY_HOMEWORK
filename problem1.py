military_time = input("What is the time?")
time = int(military_time)

if time >= 24 or time < 0:
      print("ERROR")
elif time < 9:
      print(f'"Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."')
elif time <= 16:
    print("Working hard or hardly working?")
elif time < 20:
    print( "How did it get so late so soon?")
elif time < 22:
    print("A day without sunshine is like, you know, night.")
elif time >=22:
    print( "Burning the midnight oil!")
