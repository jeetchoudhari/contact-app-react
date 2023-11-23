document.addEventListener('DOMContentLoaded', function () {
    const cardsDict = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10};
    let pSum = 0;
    let cSum = 0;
    let flag = 0;

    function drawCard(player) {
        const cardKey = getRandomKey(cardsDict);
        const cardValue = cardsDict[cardKey];
        const cardElement = document.createElement('div');
        cardElement.textContent = `Card drawn by ${player} is: ${cardKey}`;
        document.getElementById(`${player.toLowerCase()}-cards`).appendChild(cardElement);

        return cardValue;
    }

    function getRandomKey(dictionary) {
        const keys = Object.keys(dictionary);
        return keys[Math.floor(Math.random() * keys.length)];
    }

    function updateResult(message) {
        document.getElementById('result').textContent = message;
    }

    function checkWinner() {
        if (pSum > 21 || (cSum > pSum && cSum <= 21)) {
            updateResult('Computer wins!');
        } else if (pSum === cSum) {
            updateResult('Game tied!');
        } else {
            updateResult('Player wins!');
        }
    }

    function computerTurn() {
        while (cSum < 17) {
            const computerValue = drawCard('Computer');
            cSum += computerValue;
            if (cSum > 21) {
                updateResult('Player wins! Computer busted.');
            }
        }
        checkWinner();
    }

    document.getElementById('draw-btn').addEventListener('click', function () {
        if (flag === 0) {
            const playerValue = drawCard('Player');
            pSum += playerValue;
            if (pSum === 21) {
                updateResult('Player wins! Blackjack!');
                flag = 4;
            } else if (pSum > 21) {
                updateResult('Computer wins! Player busted.');
                flag = 3;
            }
        }
    });

    document.getElementById('stop-btn').addEventListener('click', function () {
        flag = 0;
        computerTurn();
    });

    // Initial computer and player draws
    for (let i = 0; i < 2; i++) {
        cSum += drawCard('Computer');
        pSum += drawCard('Player');
    }

    updateResult('After drawing two cards');
    updateResult(`Computer's total sum is ${cSum}`);
    updateResult(`Player's total sum is ${pSum}`);
});
