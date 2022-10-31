function inicio(){
    alert("Bora jogar um game de adivinhação de número!?");
    alert("Você tem 6 tentativas para adivinhar o número...");
    var nome = prompt('Qual é o seu nome para darmos início?');
    while (nome == ''){
        var nome = prompt('Qual é o seu nome para darmos início?');
    }
    document.write('<h1> Olá: ' +nome+ '!</h1>');
}

function game(){
    var num = Math.floor(Math.random() * 20) + 1;
    var tentativas = 0;

    while (numUser != num && tentativas < 6){
        tentativas++;
        var numUser = prompt('Tentativa ' + tentativas + ': Insira um número de 1 até 20, por favor:');

        while (numUser == ''){
            var numUser = prompt('Tentativa ' + tentativas + ': Insira um número de 1 até 20, por favor:');
        }
        if (num == numUser){
            alert('Você acertou!!!');
            document.write('<h1> O numero era: ' +num+ '!</h1>');
            break
        }
        else if (num > numUser){
            alert('Chutou baixo! Continue tentando...');
        }
        else if (num < numUser){
            alert('Chutou muito alto! Continue tentando...');
        }
        
    }

        if (tentativas >= 6){
            alert('Essa foi a sua ultima tentativa! Reinicie para jogar novamente. Até mais!');
            document.write('<h1> O numero era: ' +num+ '!</h1>');
        } else if (tentativas < 6){
            alert('Você venceu em menos de 6 tentativas! Parabéns! Reinicie para jogar novamente.');
        }
}

inicio()
game()
