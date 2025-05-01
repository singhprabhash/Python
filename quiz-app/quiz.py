import json;

class Quiz:

  def __init__(self):
    self.jsonData = None
    self.score = 0

  def readFile(self):
    with open('quizData.json', 'r') as file:
      """
      json.load --> Deserialize fp (a .read()-supporting file-like object containing
      a JSON document) to a Python object.
      """
      self.jsonData = json.load(file)

  def play(self):
    self.readFile()
    for question in self.jsonData:
      print("\n" + question["question"])
      for option in question["options"]:
        print(option)
      answer = input("Your answer (A/B/C/D): ").upper()
      if answer == question["answer"]:
        print("✅ Correct!")
        self.score += 1
      else:
        print(f"❌ Wrong! The correct answer was {question['answer']}")
    print(f"\n🎉 Quiz completed! Your score: {self.score}/{len(self.jsonData)}")

quiz = Quiz()
quiz.play()