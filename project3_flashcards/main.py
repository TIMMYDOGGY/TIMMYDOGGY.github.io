import random
#Load Flashcards in
import json
import os
#We did everything to get ready now just ask the questions more. 

change = 0
right = 0
number = 0
sense = False
sense_two = False
wrong = []
name = input("What is your name?")
def activate_neuron():
  global change
  global right
  global number 
  global sense
  global sense_two
  global wrong
  print("Hello!")
  if sense == True:
    f = input("I sense that you were here before! Would like to use our SPECIAL program where you will get asked the questions that you got wrong last time. Yes(1) or No(2)")  
    if f == "1":
      with open('flashcards (copy).json','r') as f:
        data = json.load(f)
      with open(f"{name}(times).json","r") as f:
        data_two = json.load(f)
      keys_two = list(data_two.keys())
      keys = list(data.keys())
      random.shuffle(keys_two)
      random.shuffle(keys)
      for key in keys_two:
        print(keys_two[change])
        a = input("What is answer?")
        if a == data_two[keys_two[change]]:
          print("Well done!")
          change += 1
          right += 1
        else:
          print("WRONG!")
          if change < len(keys_two):
            wrong.append(key)
          change += 1
      change = 0
      os.remove(f"{name}(times).json")
      wrong = []
      t = input("You have completed the questions you had trouble with last time! Good Job! Now would like to go from the start? Yes(1) or No(2). Either way your personal file will be deleted and be replaced by the next user!")
      if t =="1":
        sense = False
        for key in keys:
          print(keys[change])
          a = input("What is answer?")
          if a == data[keys[change]]:
            print("Well done!")
            change += 1
            right += 1
          else:
            print("WRONG!")
            if change < len(keys):
              wrong.append(key)
            change += 1
        change = 0
        print(f"You got {right}/12 correct!!!!")
        if right < 12:
            print("You got the following questions wrong:")
            random.shuffle(wrong)
            wrong_dict = {}
            for wrong_question in wrong: 
              wrong_dict[wrong_question] = data[wrong_question]
              print(f"{wrong_question} == {data[wrong_question]}")
              number += 1
            with open(f"{name}(times).json","w") as f:
              json.dump(wrong_dict,f)
              print("Your personal file has been updated")
            number = 0
            again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
        else:
            right = 0
            again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
              sense += 1
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
      else:
        print("Have a nice day!")
        os.remove(f"{name}(times).json")
        sense = False
    else:
        print("I did not expect for you to chose that. Well I am going to restart everything for you!")
        os.remove(f"{name}(times).json")
        wrong = []
        d = input("What would you like study? Simple(1) or Semi hard(2) math")
        if d == "1":
          with open('flashcards (copy).json','r') as f:
            data = json.load(f)
          keys = list(data.keys())
          random.shuffle(keys)
          for key in keys:
            print(keys[change])
            a = input("What is answer?")
            if a == data[keys[change]]:
              print("Well done!")
              change += 1
              right += 1
            else:
              print("WRONG!")
              if change < len(keys):
                wrong.append(key)
              change += 1
          change = 0
          number = 0
          print(f"You got {right}/12 correct!!!!")
          if right < 12:
            print("You got the following questions wrong:")
            random.shuffle(wrong)
            wrong_dict = {}
            for wrong_question in wrong: 
              wrong_dict[wrong_question] = data[wrong_question]
              print(f"{wrong_question} == {data[wrong_question]}")
              number += 1
            with open(f"{name}(times).json","w") as f:
              json.dump(wrong_dict,f)
              print("Your personal file has been updated")
            number = 0
            again = input("Congratulations! You answered all the questions! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
          else:
            right = 0
            again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
              sense += 1
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
        else:
          with open('flachcards(times).json','r') as f:
            data = json.load(f)
          keys = list(data.keys())
          random.shuffle(keys)
          for key in keys:
            print(keys[change])
            a = input("What is answer?")
            if a == data[keys[change]]:
              print("Well done!")
              change += 1
              right += 1
            else:
              print("WRONG!")
              if change < len(keys):
                wrong.append(key)
              change += 1
          change = 0
          number = 0
          print(f"You got {right}/15 correct!!!!")
          if right < 15:
            print("You got the following questions wrong:")
            random.shuffle(wrong)
            wrong_dict = {}
            for wrong_question in wrong: 
              wrong_dict[wrong_question] = data[wrong_question]
              print(f"{wrong_question} == {data[wrong_question]}")
              number += 1
            with open(f"{name}(times).json","w") as f:
              json.dump(wrong_dict,f)
              print("Your personal file has been updated")
            number = 0
            again = input("Congratulations! You answered all the questions! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
          else:
            right = 0
            again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
            if again == "1":
              activate_neuron()
              sense += 1
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
  else:
    d = input("What would you like study? Simple(1) or Semi hard(2) math?")
    if d == "1":
      with open('flashcards (copy).json','r') as f:
        data = json.load(f)
      keys = list(data.keys())
      random.shuffle(keys)
      for key in keys:
        print(keys[change])
        a = input("What is answer?")
        if a == data[keys[change]]:
          print("Well done!")
          change += 1
          right += 1
        else:
          print("WRONG!")
          if change < len(keys):
            wrong.append(key)
          change += 1
      change = 0
      print(f"You got {right}/12 correct!!!!")
      if right < 12:
          print("You got the following questions wrong:")
          random.shuffle(wrong)
          wrong_dict = {}
          for wrong_question in wrong: 
            wrong_dict[wrong_question] = data[wrong_question]
            print(f"{wrong_question} == {data[wrong_question]}")
            number += 1
          with open(f"{name}(times).json","w") as f:
            json.dump(wrong_dict,f)
            print("Your personal file has been updated")
          number = 0
          again = input("Congratulations! You have gotten through every question! Do you wanna try again? Now that you have gotten through the questions the first time you will be asked some new things. Yes(1) or No(2)")
          if again == "1":
            sense = True
            activate_neuron()
          elif again == "2":
            print("Have a nice day!")
            os.remove(f"{name}(times).json")
      else:
          right = 0
          again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
          if again == "1":
            activate_neuron()
          elif again == "2":
            print("Have a nice day!")
    elif d == "2":   
      if sense_two == True:
        f = input("I sense that you were here before! Would like to use our SPECIAL program where you will get asked the questions that you got wrong last time. Yes(1) or No(2)")  
        if f == "1":
          with open('flachcards(times).json','r') as f:
            data = json.load(f)
          with open(f"{name}(times).json","r") as f:
            data_two = json.load(f)
          keys_two = list(data_two.keys())
          keys = list(data.keys())
          random.shuffle(keys_two)
          random.shuffle(keys)
          for key in keys_two:
            print(keys_two[change])
            a = input("What is answer?")
            if a == data_two[keys_two[change]]:
              print("Well done!")
              change += 1
              right += 1
            else:
              print("WRONG!")
              if change < len(keys_two):
                wrong.append(key)
              change += 1
          t = input("You have completed the questions you had trouble with last time! Good Job! Now would like to go from the start? Yes(1) or No(2). Either way your personal file will be deleted and be replaced by the next user!")
          if t =="1":
            sense_two = False 
            for key in keys:
              print(keys[change])
              a = input("What is answer?")
              if a == data[keys[change]]:
                print("Well done!")
                change += 1
                right += 1
              else:
                print("WRONG!")
                if change < len(keys):
                  wrong.append(key)
                change += 1
            change = 0
            print(f"You got {right}/15 correct!!!!")
            if right < 15:
                print("You got the following questions wrong:")
                random.shuffle(wrong)
                wrong_dict = {}
                for wrong_question in wrong: 
                  wrong_dict[wrong_question] = data[wrong_question]
                  print(f"{wrong_question} == {data[wrong_question]}")
                  number += 1
                os.remove(f"{name}(times).json")
                with open(f"{name}(times).json","w") as f:
                  json.dump(wrong_dict,f)
                  print("Your personal file has been updated")
                number = 0
                again = input("Congratulations! You finished all the questions! Wanna try again? Yes(1) or No(2)")
                if again == "1":
                  activate_neuron()
                elif again == "2":
                  print("Have a nice day!")
                  os.remove(f"{name}(times).json")
            else:
                right = 0
                again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
                if again == "1":
                  activate_neuron()
                elif again == "2":
                  print("Have a nice day!")
                  os.remove(f"{name}(times).json")
          else:
            print("Have a nice day!")
            os.remove(f"{name}(times).json")
            sense_two = False
        else:
            print("I did not expect for you to chose that. Well I am going to restart everything for you!")
            os.remove(f"{name}(times).json")
            d = input("What would you like study? Simple(1) or Semi hard(2) math")
            with open('flachcards(times).json','r') as f:
              data = json.load(f)
            if d == "1":
              keys = list(data.keys())
              random.shuffle(keys)
              for key in keys:
                print(keys[change])
                a = input("What is answer?")
                if a == data[keys[change]]:
                  print("Well done!")
                  change += 1
                  right += 1
                else:
                  print("WRONG!")
                  if change < len(keys):
                    wrong.append(key)
                  change += 1
              change = 0
              print(f"You got {right}/15 correct!!!!")
              if right < 15:
                print("You got the following questions wrong:")
                random.shuffle(wrong)
                wrong_dict = {}
                for wrong_question in wrong: 
                  wrong_dict[wrong_question] = data[wrong_question]
                  print(f"{wrong_question} == {data[wrong_question]}")
                  number += 1
                with open(f"{name}(times).json","w") as f:
                  json.dump(wrong_dict,f)
                  print("Your personal file has been updated")
                number = 0
                again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
                if again == "1":
                  activate_neuron()
                elif again == "2":
                  print("Have a nice day!")
                  os.remove(f"{name}(times).json")
              else:
                right = 0
                again = input("Congratulations! You got all the questions right! Wanna try again? Yes(1) or No(2)")
                if again == "1":
                  activate_neuron()
                  sense += 1
                elif again == "2":
                  print("Have a nice day!")
                  os.remove(f"{name}(times).json")
      else:
        with open('flachcards(times).json','r') as f:
          data = json.load(f)
        keys = list(data.keys())
        random.shuffle(keys)
        for key in keys:
          print(keys[change])
          a = input("What is answer?")
          if a == data[keys[change]]:
            print("Well done!")
            change += 1
            right += 1
          else:
            print("WRONG!")
            if change < len(keys):
              wrong.append(key)
            change += 1
        change = 0
        print(f"You got {right}/15 correct!!!!")
        if right < 15:
            print("You got the following questions wrong:")
            random.shuffle(wrong)
            wrong_dict = {}
            for wrong_question in wrong: 
              wrong_dict[wrong_question] = data[wrong_question]
              print(f"{wrong_question} == {data[wrong_question]}")
              number += 1
            with open(f"{name}(times).json","w") as f:
              json.dump(wrong_dict,f)
              print("Your personal file has been updated")
            number = 0
            again = input("Congratulations! You have gotten through every question! Do you wanna try again? Now that you have gotten through the questions the first time you will be asked some new things. Yes(1) or No(2)")
            if again == "1":
              sense = True
              activate_neuron()
            elif again == "2":
              print("Have a nice day!")
              os.remove(f"{name}(times).json")
activate_neuron()