
from flask import Blueprint, render_template, url_for, redirect, current_app
from flask_mail import Mail, Message
from webapp.user.models import User
from webapp.config import MAIL_DEFAULT_SENDER


blueprint = Blueprint('email', __name__, url_prefix='/email')


@blueprint.route('/send-first-msg')
def send_welcome_email(email_to):
    with current_app.app_context():
        app = current_app._get_current_object()
        mail = Mail(app)
        user = User.query.filter_by(email=email_to).first()
        if not user:
            return redirect(url_for('users.login'))
        msg = Message(sender=MAIL_DEFAULT_SENDER,
                      recipients=[email_to])
        welcome_email = render_template('email/welcome.html', user=user)
        msg.html = welcome_email
        mail.send(msg)
        return redirect(url_for('users.login'))
