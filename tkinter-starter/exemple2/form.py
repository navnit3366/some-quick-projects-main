import tkinter as tk



########questions
Questionnaires = [
    (
        "Quelle est la capitale de la France ?",
        ("Marseille", "Nice", "Paris", "Nantes", "Lille"),
        "Paris"
    ),
    (
        "Quelle est la capitale de l'Italie ?",
        ("Rome", "Venise", "Pise", "Florence"),
        "Rome"
    ),
    (
        "Quelle est la capitale de la Belgique ?",
        ("Anvers", "Bruxelles", "Bruges", "Liège"),
        "Bruxelles"
    )
]


########scores
Liste_scores = { elt[0]:0 for elt in Questionnaires }
globals()['SCORE'] = 0
def validate_answer(choice, questionnaire):
    score = 0
    question_, reponses, bonne_rep = questionnaire
    return 1 if choice==bonne_rep else 0
def set_score_on_resp(note,id_):
    Liste_scores[Questionnaires[id_][0]] = note
def set_global_score():
    globals()['SCORE'] = sum(Liste_scores.values())
    return globals()['SCORE']
    
def validate_choice(choice, id_=None):
   if id_ is None: raise Exception('pb')
   print(f"q{1+id_} response chosen: {choice}")
   note = validate_answer(choice,Questionnaires[id_])  # 0 or 1
   set_score_on_resp(note, id_)
   global_score = set_global_score()
   return global_score
   


#####affichages
root = tk.Tk()

for id_ in range(len(Questionnaires)):
    
    tup = Questionnaires[id_] #un questionaire
    
    # question
    message = tk.Label(root, text=tup[0]) #la question à afficher
    message['text'] = tup[0]
    message.pack() #add to screen
    
    # reponses possibles
    Liste_reponses = tup[1] # les reponses possibles
    reponse = tk.StringVar() # la reponses du user
    reponse.set(tup[2])
    def handle_answers2(choice, id_=id_):
        global_score = validate_choice(choice=choice, id_=id_)
        rep_label['text'] = f"score: {global_score}"
    opt = tk.OptionMenu( # la reponses possibles à afficher
        root,
        reponse,
        *Liste_reponses,
        command = handle_answers2
    )
    opt.pack(expand=True)

# place a label on the root window
rep_label = tk.Label(root, text="score")
rep_label.pack()
rep_label['text'] = f"score: noscore"


root.mainloop()