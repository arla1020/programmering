<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<title>Blackjack 2D – Multiplayer</title>
<style>
body {
    margin: 0;
    background: #0b3d1e;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
}
canvas {
    background: #0f6b32;
    display: block;
    margin: auto;
    border: 3px solid black;
}
button {
    font-size: 18px;
    padding: 10px 20px;
    margin: 10px;
    cursor: pointer;
}
</style>
</head>
<body>

<h1>BLACKJACK</h1>
<canvas id="game" width="900" height="500"></canvas><br>

<button onclick="hit()">HIT</button>
<button onclick="stand()">STAND</button>
<button onclick="restart()">RESTART</button>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const CARD_VALUES = {
    A:11, K:10, Q:10, J:10,
    10:10, 9:9, 8:8, 7:7,
    6:6, 5:5, 4:4, 3:3, 2:2
};

let deck = [];
let players = [];
let dealer = [];
let currentPlayer = 0;
let gameOver = false;
let message = "";

function askPlayers() {
    players = [];
    for (let i = 1; i <= 3; i++) {
        let name = prompt(`Skriv namn för Player ${i} (Enter för att hoppa över)`);
        if (!name) break;
        players.push({ name: name, hand: [], done: false });
    }
    if (players.length === 0) {
        alert("Minst 1 spelare krävs!");
        askPlayers();
    }
}

function newDeck() {
    deck = [];
    for (let c in CARD_VALUES) {
        for (let i = 0; i < 4; i++) deck.push(c);
    }
    deck.sort(() => Math.random() - 0.5);
}

function handValue(hand) {
    let total = 0;
    let aces = 0;
    for (let c of hand) {
        total += CARD_VALUES[c];
        if (c === "A") aces++;
    }
    while (total > 21 && aces) {
        total -= 10;
        aces--;
    }
    return total;
}

function deal() {
    newDeck();
    dealer = [deck.pop(), deck.pop()];
    for (let p of players) {
        p.hand = [deck.pop(), deck.pop()];
        p.done = false;
    }
    currentPlayer = 0;
    gameOver = false;
    message = "";
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.font = "22px Arial";
    let y = 50;

    for (let i = 0; i < players.length; i++) {
        let p = players[i];
        ctx.fillText(
            `${p.name}${i === currentPlayer && !gameOver ? " ← TUR" : ""}`,
            40, y
        );
        ctx.fillText(p.hand.join("  "), 40, y + 30);
        ctx.fillText("Värde: " + handValue(p.hand), 40, y + 60);
        y += 110;
    }

    ctx.fillText("Dealer:", 500, 50);
    if (gameOver) {
        ctx.fillText(dealer.join("  "), 500, 80);
        ctx.fillText("Värde: " + handValue(dealer), 500, 110);
    } else {
        ctx.fillText("??", 500, 80);
    }

    ctx.font = "28px Arial";
    ctx.fillText(message, 250, 460);
}

function nextPlayer() {
    players[currentPlayer].done = true;
    currentPlayer++;
    if (currentPlayer >= players.length) dealerTurn();
}

function hit() {
    if (gameOver) return;
    let p = players[currentPlayer];
    p.hand.push(deck.pop());
    if (handValue(p.hand) > 21) nextPlayer();
    draw();
}

function stand() {
    if (gameOver) return;
    nextPlayer();
    draw();
}

function dealerTurn() {
    while (handValue(dealer) < 17) dealer.push(deck.pop());

    let dealerVal = handValue(dealer);
    let results = [];

    for (let p of players) {
        let pv = handValue(p.hand);
        if (pv > 21) results.push(`${p.name} bustade`);
        else if (dealerVal > 21 || pv > dealerVal) results.push(`${p.name} vann`);
        else if (pv === dealerVal) results.push(`${p.name} oavgjort`);
        else results.push(`${p.name} förlorade`);
    }

    message = results.join(" | ");
    gameOver = true;
}

function restart() {
    askPlayers();
    deal();
    draw();
}

askPlayers();
deal();
draw();
</script>

</body>
</html>
