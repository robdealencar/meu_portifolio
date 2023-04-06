const form = document.querySelector('#form-contato');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const nome = document.querySelector('#nome').value;
  const email = document.querySelector('#email').value;
  const mensagem = document.querySelector('#mensagem').value;

  const data = new FormData();
  data.append('nome', nome);
  data.append('email', email);
  data.append('mensagem', mensagem);

  fetch('enviar-email.php', {
    method: 'POST',
    body: data
  })
    .then(response => {
      if (response.ok) {
        alert('Email enviado com sucesso!');
      } else {
        throw new Error('Ocorreu um erro ao enviar o email.');
      }
    })
    .catch(error => {
      console.error(error);
      alert(error.message);
    });
});
