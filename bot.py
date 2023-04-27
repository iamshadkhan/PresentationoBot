import nltk

from nltk.chat.util import Chat

pairs = [
 
[r"data science",
 ["Please Select a Sub-topic You want for your presentation \n Data Mining",]
],
[r"Data Mining",
 ["Data Mining is the process of extracting useful information from large sets of structured or unstructured data. It involves techniques such as clustering, classification, and regression analysis to identify patterns and relationships within the data.",]
],

]

[] 
def chat():
      print("Hi! I am PresentationoBot for your service\n Please Select a topic given below \n 'Data Science','A.I','M.L','IOT','C.S'")
      chat = Chat(pairs)
      chat.converse()

[]
if __name__== "__main__":
     chat()


[]