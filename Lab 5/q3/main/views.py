from django.shortcuts import render
from .forms import CaptchaForm

def captcha_view(request):
    captcha = "X9aB2"
    msg = ''
    locked = False

    # track failures using session
    if 'fails' not in request.session:
        request.session['fails'] = 0

    form = CaptchaForm()

    if request.method == "POST":
        if request.session['fails'] >= 3:
            locked = True
        else:
            form = CaptchaForm(request.POST)
            if form.is_valid():
                user_input = form.cleaned_data['input_text']
                if user_input == captcha:
                    msg = "Captcha Matched!"
                    request.session['fails'] = 0
                else:
                    request.session['fails'] += 1
                    msg = f"Wrong! Attempts: {request.session['fails']}"
                    if request.session['fails'] >= 3:
                        locked = True

    return render(request, 'main/captcha.html', {
        'form': form, 'captcha': captcha, 'msg': msg, 'locked': locked
    })