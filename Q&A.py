#I learned how to create this from this website "https://www.askpython.com/python/examples/easy-games-in-python"
while True:
  print('Are you a true One Piece fan? Test yourself in this questionnaire!')
  answer = input('Are you ready to check your One Piece knowledge? (yes/no) ')
  score = 0
  total_questions = 5

  if answer.lower() == 'yes':
    answer_1 = input('Question 1: What is the name of the island where the One Piece located?')
    if answer_1.lower() == 'laughtale' or answer_1.lower() == 'laugh tale' or answer_1.lower() =='raphtal':
        print("Correct!")
        score += 1
    else:
      print('That is incorrect.')
      
  if answer.lower() == 'yes':
    answer_2 = input('Question 2: What is the name of the sword Zoro got in the Land of Wano? ')
    if answer_2.lower() == 'enma':
      print("Correct!")
      score += 1
    else:
      print('That is incorrect.')

  if answer.lower() == 'yes':
    answer_3 = input('Question 3: When was Luffys awakening first forshadowed? ')
    if answer_3.lower() == 'skypea' or answer_3.lower() == 'Skypea' or answer_3.lower() == 'sky isnland':
      print("Correct!")
      score += 1
    else:
      print('That is incorrect.')

  if answer.lower() == 'yes':
    answer_4 = input('Question 4: In which Devil fruit type is Luffys devil fruit?')
    if answer_4.lower() == 'zoan' or answer_4.lower() == 'zoan-type':
      print("Correct!")
      score += 1
    else:
      print('That is incorrect.')
      
  if answer.lower() == 'yes':
    answer_5 = input('Question 5: How many awakend Zoan type users are there?')
    if answer_5.lower() == '7':
      print("Correct!")
      score += 1
    else:
      print('That is incorrect.')
          
  print('Thank you for playing this small quiz. You answered', score, 'questions correctly!')
  mark = (score / total_questions) * 100
  print('Marks obtained:', mark)
  if mark >= 50:
    print('Your are a true one piece fan. Be proud!')
  else:
    print('You did not get a good score.')
    play_again = input('Would you like to play again?(yes/no): ')
    if play_again.lower() != 'yes':
      break
