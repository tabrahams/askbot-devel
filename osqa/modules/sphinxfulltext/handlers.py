from osqa.models import Question

def question_search(keywords):
    return Question.search.query(keywords)