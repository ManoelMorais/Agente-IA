def build_prompt(modo, nivel, texto):
    if modo == "Correção guiada":
        return f"Level {nivel}: Correct and explain '{texto}', then give a short practice task."
    elif modo == "Treino CEFR":
        return f"Level {nivel}: Create an exam-style task based on '{texto}', with model answer and rubric."
    else:  # Vocabulário
        return f"Level {nivel}: Generate 8 flashcards with word, definition, example, collocations. Theme: {texto}"