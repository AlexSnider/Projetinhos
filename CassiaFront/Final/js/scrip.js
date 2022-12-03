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

function mCpf() {
   var cpf = event.target.value;
   cpf = cpf.replace(/\D/g, "")
   cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2")
   cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2")
   cpf = cpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2")
   event.target.value = cpf;
}

function validarCPF() {
   var cpf = event.target.value;
   var ok = 1;
   var add;
   if (cpf != "") {
      cpf = cpf.replace(/[^\d]+/g, '');
      if (cpf.length != 11 ||
         cpf == "00000000000" ||
         cpf == "11111111111" ||
         cpf == "22222222222" ||
         cpf == "33333333333" ||
         cpf == "44444444444" ||
         cpf == "55555555555" ||
         cpf == "66666666666" ||
         cpf == "77777777777" ||
         cpf == "88888888888" ||
         cpf == "99999999999")
             ok = 0;
      if (ok == 1) {
         add = 0;
         for (i = 0; i < 9; i++)
            add += parseInt(cpf.charAt(i)) * (10 - i);
            rev = 11 - (add % 11);
            if (rev == 10 || rev == 11)
               rev = 0;
            if (rev != parseInt(cpf.charAt(9)))
               ok = 0;
            if (ok == 1) {
               add = 0;
               for (i = 0; i < 10; i++)
                  add += parseInt(cpf.charAt(i)) * (11 - i);
               rev = 11 - (add % 11);
               if (rev == 10 || rev == 11)
                  rev = 0;
               if (rev != parseInt(cpf.charAt(10)))
                  ok = 0;
            }
        }
        if (ok == 0) {
           alert("Ops... Ocorreu um problema... CPF inválido!");
           event.target.focus();
        }
    }
}

function mMoeda () {
   var v = event.target.value;
   v = v.replace(/\D/g, "");
   v = v.replace(/^0+/g, "");
   v = v.replace(/(\d{1})(\d{13})$/, "$1.$2");
   v = v.replace(/(\d{1})(\d{10})$/, "$1.$2");
   v = v.replace(/(\d{1})(\d{7})$/, "$1.$2");
   v = v.replace(/(\d{1})(\d{4})$/, "$1.$2");
   v = v.replace(/(\d{1})(\d{1,1})$/, "$1,$2");
   event.target.value = v;
 }

function validate_password(){
   var pass = document.getElementById('senha').value;
   var confirm_pass = document.getElementById('senha1').value;
   var nome = document.getElementById('first-name').value;
   var sobrenome = document.getElementById('second-name').value;
   var email = document.getElementById('email'). value;
   var telefone = document.getElementById('telefone').value;
   var cpf = document.getElementById('cpf').value;
   var text = document.getElementById('Form-text-description').value;


   if (nome && sobrenome && email && telefone && cpf && pass && text && confirm_pass != ''){
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
