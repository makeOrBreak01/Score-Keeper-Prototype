count =  {"strikes":0,
          "balls":0}
#next step, handling hits, outs and baserunners.

#balls and strikes
def end_at_bat(count=count, in_play=False):
    if count["strikes"] >= 3:
        print("Strikeout!")
        return True
    elif count["balls"] >= 4:
        print("Ball four, take your base.")
        return True
    elif in_play == True:
        return True
    else:
        return False
        
def next_pitch_prompt():
    print("Here come's the pitch...")
    pitch = input("Strike = S | Ball = B | Foul = F | In Play = I  ").casefold()
    pitch_in_play = False
    if pitch == "s":
        print("Strike!")
        count["strikes"] += 1
    elif pitch == "b":
        print("Ball!")
        count["balls"] += 1
    elif pitch == "f":
        print("Foul ball!")
        if count["strikes"] < 2:
            count["strikes"] += 1
    elif pitch == "i":
        in_play_result = input("Enter the play result:")
        pitch_in_play = True
    else:
        print("please enter a valid pitch result")

    
    if end_at_bat(count, pitch_in_play) == False:
        print("The count is: " + str(count["balls"]) + " balls and " + str(count["strikes"]) + " strikes.")
    else:
        count.update(strikes=0, balls=0)
        print("Batter up!")
    print()
    next_pitch_prompt()
        


next_pitch_prompt()
