from django.shortcuts import render, redirect
from .models import Question
from .forms import QuizForm

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['correct_answer']
            correct_answer = form.instance.correct_answer
            if user_answer == correct_answer:
                feedback = "Your answer is correct!"
            else:
                feedback = f"Sorry, the correct answer is {correct_answer}."
            return render(request, 'quiz_result.html', {'feedback': feedback})
    else:
        form = QuizForm()
    
    return render(request, 'quiz.html', {'form': form})