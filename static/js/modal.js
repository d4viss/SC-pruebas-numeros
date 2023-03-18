const open = document.getElementById('open');
const modal_container = document.getElementById('modal_container');
const close = document.getElementById('close');

const fileInput = document.getElementById('input-file');

open.addEventListener('click', () => {
  modal_container.classList.add('show');
});

close.addEventListener('click', () => {
  modal_container.classList.remove('show');
});

fileInput.addEventListener('change', () => {
  const fileName = fileInput.value
  const fileExtension = fileName.split('.').pop();
  if (fileName !== '' && fileExtension == "csv") {
    close.disabled = false;
  } else {
    close.disabled = true;
  }
});