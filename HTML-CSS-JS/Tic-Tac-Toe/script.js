document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    const resultElement = document.getElementById('result');
    const turnElement = document.getElementById('turn');
    let currentPlayer = 'X';
    let gameBoard = ['', '', '', '', '', '', '', '', ''];
    let gameActive = true;

    function checkWinner() {
        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];

        for (let pattern of winPatterns) {
            const [a, b, c] = pattern;
            if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
                return gameBoard[a];
            }
        }

        return gameBoard.includes('') ? null : 'T';
    }

    function handleCellClick(index) {
        if (!gameActive || gameBoard[index] !== '') return;

        gameBoard[index] = currentPlayer;
        renderBoard();

        const winner = checkWinner();
        if (winner) {
            gameActive = false;
            setTimeout(() => showResult(winner), 500);
        } else {
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            updateTurn();
        }
    }

    function updateTurn() {
        turnElement.textContent = `Player ${currentPlayer}'s turn`;
    }

    function renderBoard() {
        board.innerHTML = '';
        gameBoard.forEach((value, index) => {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.textContent = value;
            cell.addEventListener('click', () => handleCellClick(index));
            board.appendChild(cell);
        });
    }

    function showResult(winner) {
        if (winner === 'T') {
            resultElement.textContent = "It's a tie!";
        } else {
            resultElement.textContent = `Player ${winner} wins!`;
        }

        board.style.display = 'none';
        turnElement.style.display = 'none';
        resultElement.style.display = 'block';
    }

    window.resetGame = function () {
        currentPlayer = 'X';
        gameBoard = ['', '', '', '', '', '', '', '', ''];
        gameActive = true;
        resultElement.textContent = '';
        updateTurn();
        board.style.display = 'grid';
        turnElement.style.display = 'block';
        resultElement.style.display = 'none';
        renderBoard();
    };

    updateTurn();
    renderBoard();
});
