function chars(){
   var name = event.target.value;
   name = name.replace(/\d/g, '')
   event.target.value = name;
}

function validaEmail(e) {
   var filter = /^\s*[\w\-\+_]+(\.[\w\-\+_]+)*\@[\w\-\+_]+\.[\w\-\+_]+(\.[\w\-\+_]+)*\s*$/;
   if (String(e).search (filter) == -1)
      alert('Seu email parece não estar no formato correto. Por favor, corrija.')
}

function mTel () {
   var tel = event.target.value;
   tel = tel.replace(/\D/g, "")
   tel = tel.replace(/^(\d)/, "($1")
   tel = tel.replace(/(.{3})(\d)/, "$1)$2")
   if (tel.length == 10) {
      tel = tel.replace(/(.{1})$/, "-$1")
   } else if (tel.length == 11) {
      tel = tel.replace(/(.{2})$/, "-$1")
   } else if (tel.length == 12) {
      tel = tel.replace(/(.{3})$/, "-$1")
   } else if (tel.length == 13) {
      tel = tel.replace(/(.{4})$/, "-$1")
   } else if (tel.length > 14) {
      tel = tel.replace(/(.{4})$/, "-$1")
   }
   event.target.value = tel;
}

function mCEP () {
   var cep = event.target.value;
   cep = cep.replace(/\D/g, "")
   cep = cep.replace(/^(\d{2})(\d)/, "$1.$2")
   cep = cep.replace(/.(\d{3})(\d)/, ".$1-$2")
   event.target.value = cep;
}

function validate_password(){
   var pass = document.getElementById('senha').value;
   var confirm_pass = document.getElementById('senha1').value;
   var nome = document.getElementById('first-name').value;
   var sobrenome = document.getElementById('second-name').value;
   var email = document.getElementById('email'). value;
   var telefone = document.getElementById('telefone').value;
   var cep = document.getElementById('zipcode').value;


   if (nome && sobrenome && email && telefone && cep && pass && confirm_pass != ''){
      alert('Os campos obrigatórios foram preenchidos!')
      if (pass == confirm_pass){
         alert('Cadastro validado e registrado!')
      }
      else{
         alert('Senhas diferentes. Por favor, verifique novamente a confirmação da senha!')
      }
   }
   else{
      alert('Parece que há campos a serem preenchidos. Por favor, complete todos.')
   }
}





