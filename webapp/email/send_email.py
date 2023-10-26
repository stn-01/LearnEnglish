
from flask import (Blueprint, render_template, url_for,
                   redirect, current_app)
from flask_mail import Mail, Message
from webapp.user.models import User
from webapp.config import MAIL_DEFAULT_SENDER


blueprint = Blueprint('email', __name__, url_prefix='/email')


def send_email(subject, template_of_email, email_to):
    with current_app.app_context():
        app = current_app._get_current_object()
        mail = Mail(app)
        user = User.query.filter_by(email=email_to).first()
        token = user.get_reset_password_token()
        msg = Message(subject=subject, sender=MAIL_DEFAULT_SENDER,
                      recipients=[email_to])
        email = render_template(template_of_email, user=user, token=token)
        msg.html = email
        mail.send(msg)


@blueprint.route('/send-first-msg')
def send_welcome_email(email_to):
    template = 'email/welcome.html'
    send_email('Приветствуем Вас на LearnEnglish', template, email_to=email_to)
    return redirect(url_for('users.login'))


def send_password_reset_email(user):
    template = 'email/reset_password_email.html'
    send_email('Сброс пароля', template, email_to=user.email)
