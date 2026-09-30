# ============================================================
#                         MINDMATE
#              Your Personal Reflection Space
# ============================================================

print("=" * 60)
print("                         MINDMATE")
print("               Your Personal Reflection Space")
print("=" * 60)

print("\nWelcome to MindMate!")

print("\nMindMate is a simple self-reflection program designed")
print("to help you slow down, organize your thoughts, and")
print("look at situations from different perspectives.")

print("\nSometimes we mix what actually happened with what we")
print("think it means. MindMate helps you separate facts from")
print("interpretations and reflect before jumping to conclusions.")

print("\nMindMate is not a therapist or a medical tool.")
print("It is simply a space for reflection and structured thinking.")

print("\nTake a breath. Let's begin.")

# ------------------------------------------------------------
# USER INTRODUCTION
# ------------------------------------------------------------

name = input("\nWhat is your name? ")

print("\nNice to meet you, " + name + ".")

print("\nLet's take a look at what's on your mind.")

# ------------------------------------------------------------
# UNDERSTANDING THE SITUATION
# ------------------------------------------------------------

event = input("\nWhat actually happened?\n> ")

interpretation = input(
    "\nWhat do you think this situation means?\n> "
)

# ------------------------------------------------------------
# EMOTION
# ------------------------------------------------------------

print("\nHow are you feeling right now?")

print("1. Sad")
print("2. Anxious")
print("3. Angry")
print("4. Lonely")
print("5. Confused")
print("6. Stressed")

emotion_choice = input("\nEnter a number from 1 to 6: ")

if emotion_choice == "1":
    emotion = "Sad"
elif emotion_choice == "2":
    emotion = "Anxious"
elif emotion_choice == "3":
    emotion = "Angry"
elif emotion_choice == "4":
    emotion = "Lonely"
elif emotion_choice == "5":
    emotion = "Confused"
elif emotion_choice == "6":
    emotion = "Stressed"
else:
    emotion = "Unspecified"

# ------------------------------------------------------------
# BELIEF STRENGTH
# ------------------------------------------------------------

print("\nHow strongly do you believe your interpretation?")

while True:
    belief_input = input("Enter a number from 1 to 10: ")

    if belief_input.isdigit():
        belief = int(belief_input)

        if 1 <= belief <= 10:
            break

    print("Please enter a number between 1 and 10.")

# ------------------------------------------------------------
# EVIDENCE
# ------------------------------------------------------------

print("\nDo you have clear evidence supporting your interpretation?")

print("1. Yes")
print("2. No")
print("3. I am not sure")

evidence_choice = input("\nEnter 1, 2, or 3: ")

if evidence_choice == "1":
    evidence = "Yes"
elif evidence_choice == "2":
    evidence = "No"
elif evidence_choice == "3":
    evidence = "Not sure"
else:
    evidence = "Not specified"

# ------------------------------------------------------------
# FACT OR ASSUMPTION
# ------------------------------------------------------------

print("\nDo you think your interpretation is mainly:")

print("1. A fact")
print("2. An assumption")
print("3. A mixture of both")

thought_choice = input("\nEnter 1, 2, or 3: ")

if thought_choice == "1":
    thought_type = "Fact"
elif thought_choice == "2":
    thought_type = "Assumption"
elif thought_choice == "3":
    thought_type = "Both"
else:
    thought_type = "Not specified"

# ------------------------------------------------------------
# ANALYSIS
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("                    YOUR REFLECTION")
print("=" * 60)

print("\nName:", name)

print("\nWHAT ACTUALLY HAPPENED:")
print(event)

print("\nWHAT YOU THINK IT MEANS:")
print(interpretation)

print("\nYOUR EMOTION:")
print(emotion)

print("\nBELIEF STRENGTH:")
print(str(belief) + "/10")

print("\nEVIDENCE:")
print(evidence)

print("\nTHOUGHT TYPE:")
print(thought_type)

# ------------------------------------------------------------
# MAIN ANALYSIS
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("                         ANALYSIS")
print("-" * 60)

if thought_type == "Assumption" and belief >= 8 and evidence == "No":

    print("\nYour interpretation feels very strong, but you")
    print("currently do not have clear evidence supporting it.")

    print("\nThis does not mean that your feelings are wrong.")
    print("It means that the conclusion may not be fully confirmed.")

    print("\nTry asking yourself:")
    print("What do I KNOW happened?")
    print("What am I ASSUMING happened?")

elif thought_type == "Assumption" and belief >= 8:

    print("\nYou strongly believe this interpretation.")
    print("However, you have identified it as an assumption.")

    print("\nTry considering whether there could be another")
    print("explanation for what happened.")

elif thought_type == "Assumption":

    print("\nYou recognize that your interpretation is an assumption.")

    print("\nThat's useful because it gives you room to consider")
    print("other possible explanations before reaching a conclusion.")

elif thought_type == "Fact":

    print("\nYou see your interpretation as being based on a fact.")

    print("\nInstead of repeatedly questioning what happened,")
    print("try thinking about what you can actually control.")

else:

    print("\nYour interpretation appears to contain both facts")
    print("and assumptions.")

    print("\nTry separating the confirmed facts from the meaning")
    print("you have attached to those facts.")

# ------------------------------------------------------------
# EVIDENCE ANALYSIS
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("                     EVIDENCE CHECK")
print("-" * 60)

if evidence == "No":

    print("\nYou currently do not have clear evidence supporting")
    print("your interpretation.")

    print("\nThere may be more than one possible explanation.")

elif evidence == "Yes":

    print("\nYou have identified evidence supporting your thought.")

    print("\nNow consider whether there is also evidence that")
    print("could point toward another explanation.")

elif evidence == "Not sure":

    print("\nYou are unsure about the evidence.")

    print("\nTry writing down exactly what happened without")
    print("adding assumptions about why it happened.")

else:

    print("\nYou did not specify whether you have evidence.")

# ------------------------------------------------------------
# EMOTION-BASED REFLECTION
# ------------------------------------------------------------

print("\n")
print("-" * 60)
print("                  PERSONAL REFLECTION")
print("-" * 60)

if emotion == "Anxious":

    print("\nWhen we feel anxious, uncertainty can sometimes")
    print("feel like certainty.")

    print("Give yourself some time before making a major conclusion.")

elif emotion == "Sad":

    print("\nIt is okay to acknowledge that the situation hurt you.")

    print("Try not to turn one painful situation into a conclusion")
    print("about your entire self-worth.")

elif emotion == "Angry":

    print("\nStrong emotions can make an immediate reaction feel necessary.")

    print("Consider giving yourself some time before responding.")

elif emotion == "Lonely":

    print("\nFeeling lonely can sometimes make a difficult situation")
    print("feel even bigger.")

    print("Consider reaching out to someone you trust.")

elif emotion == "Confused":

    print("\nYou do not have to figure everything out immediately.")

    print("Start by separating what you know from what you don't know.")

elif emotion == "Stressed":

    print("\nStress can make several problems feel like one huge problem.")

    print("Try breaking the situation into one small thing you")
    print("can deal with right now.")

else:

    print("\nTake some time to understand what you are feeling.")

# ------------------------------------------------------------
# FINAL REFLECTION
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("                    WHAT YOU CAN DO")
print("=" * 60)

print("\n1. Separate facts from assumptions.")
print("2. Consider another possible explanation.")
print("3. Focus on what you can control.")
print("4. Give yourself time before making a major decision.")
print("5. Talk to someone you trust if you need support.")

print("\nRemember:")
print("A thought can feel very real without being a confirmed fact.")

print("\n")
print("=" * 60)
print("              Thank you for using MindMate.")
print("=" * 60)