from flask import Flask, render_template, request
import random

app = Flask(__name__)

cards_dict = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    p_summ = 0
    c_summ = 0
    flag = 0
    player_cards = []
    computer_cards = []

    for i in range(0, 2):
        random_number_computer = random.choice(list(cards_dict.keys()))
        computer_cards.append(random_number_computer)
        c_summ += cards_dict[random_number_computer]

    for i in range(0, 2):
        random_number_player = random.choice(list(cards_dict.keys()))
        player_cards.append(random_number_player)
        p_summ += cards_dict[random_number_player]

    return render_template('play.html', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)

@app.route('/draw', methods=['POST'])
def draw():
    p_summ = int(request.form['player_sum'])
    c_summ = int(request.form['computer_sum'])
    print("P_summ= ", p_summ)
    print("c_summ= ", c_summ)
    player_cards = request.form.getlist('player_cards')
    computer_cards = request.form.getlist('computer_cards')
    print("Player your turn")
    if(p_summ==21):
        return render_template('result.html', result='Player wins', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)
    else:
        player_input = request.form['user_input']
        if(player_input == 'stop' or p_summ >= 21):
            flag = 0
            if p_summ == c_summ and c_summ > 16:
                return render_template('result.html', result='Game tied')
        if(player_input == 'draw'):
            flag = 1
            while flag == 1:
                random_number_player = random.choice(list(cards_dict.keys()))
                print("Card drawn by player is: ", random_number_player)
                player_cards.append(random_number_player)
                random_player_value = cards_dict[random_number_player]
                p_summ = p_summ + random_player_value
                print("Players total sum after drawing one more card is ", p_summ)
                if(p_summ > 21):
                    flag = 3
                    break
                if(p_summ==21):
                    flag =4
                    break
                return render_template('play.html', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)
        else:
            flag=0

    if(flag == 3):
        return render_template('result.html', result='Computer wins', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)
    elif(flag==4):
        return render_template('result.html', result='Player wins', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)
    elif(flag==0):
        while(c_summ<17):
            random_number_computer = random.choice(list(cards_dict.keys()))
            print("Card drawn by computer is: ", random_number_computer)
            random_computer_value = cards_dict[random_number_computer]
            c_summ = c_summ + random_computer_value
            print("Computers total sum after drawing one more card is ", c_summ)
            if(c_summ > p_summ and c_summ < 22):
                return render_template('result.html', result='Computer wins', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)
        else:
            return render_template('result.html', result='Player wins', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)

    return render_template('play.html', player_sum=p_summ, computer_sum=c_summ, player_cards=player_cards, computer_cards=computer_cards)

if __name__ == '__main__':
    app.run(debug=True)
