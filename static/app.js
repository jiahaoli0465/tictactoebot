document.querySelector('#refresh').addEventListener('click', function(e){
    e.preventDefault()
    window.location.href = '/play';
})

document.querySelector('#home').addEventListener('click', function(e){
    e.preventDefault()
    window.location.href = '/';
})

document.querySelectorAll('.cell').forEach(cell => {
    
    cell.addEventListener('click', function() {
        if (this.classList.contains('player') || this.classList.contains('computer') || gameover) {
            console.log('nope')
            return;  
        }
        let cellId = this.getAttribute('data-bid')
        
            this.classList.add('player')
            updateCellContent(this);
            console.log(`id is ${cellId}`)

            check = checkCell();


        if (!check) {
            getAI(cellId).then(isOver => {
                if (isOver) {
                    console.log('Game Over');
                    gameover = true
                } else {
                    return
                }
            });

        }

        



    });
});

function checkCell() {
    let allCellTaken = true;
    const cells = document.querySelectorAll('.cell');

    for (const cell of cells) {
        if (!cell.classList.contains('player') && !cell.classList.contains('computer')) {
            allCellTaken = false;
            break;
        }
    }

    return allCellTaken;
}

function updateCellContent(cell) {
    if (cell.classList.contains('player')) {
        cell.textContent = 'X';
    } else if (cell.classList.contains('computer')) {
        cell.textContent = 'O';
    }
}



function getAI(cellId) {
    return new Promise((resolve, reject) => {
        axios.post('/move', { bid: cellId })
        .then(response => {
            const action = response.data;
            const bid = action['action'];
            const message = action['message'];

            console.log(bid);
            console.log(message);

            let cell = document.querySelector(`[data-bid='${bid}']`);
            cell.classList.add('computer');
            updateCellContent(cell);

            if (message === 'over') {
                gameover = true;
            }

            resolve(message === 'over');
        })
        .catch(error => {
            console.error('Error:', error);
            reject(error);
        });
    });
}


let gameover = false;
