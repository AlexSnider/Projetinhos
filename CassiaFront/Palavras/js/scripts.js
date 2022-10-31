var vetor = []
alert('Olá, digite uma palavra e guardarei pra você!');
    var userInput = true
    while (userInput){
        palavra = prompt('Insira quantas palavras quiser e se repetir alguma, te mostro o que já guardei:');
if (vetor.includes(palavra)){
    alert('Ops! Essa palavra já existe!'), 
    alert('Reinicie o programa para guardar novas Palavras. Guardei essas palavras pra você!'), document.write(vetor), console.log(vetor)
    break
}else
    vetor.push(palavra)
}
