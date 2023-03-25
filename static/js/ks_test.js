const tableDiv = document.getElementById('table-div');
const table = document.querySelector('table');
const tableResult = document.getElementById('table-results');
const tableDiff = document.getElementById('table-diff');
const spanResultTrue = document.getElementById('span-result-true');
const spanResultFalse = document.getElementById('span-result-false');
const lblValidation = document.getElementById('lbl_validation');
const submitBtn = document.getElementById('submitBtn');
const fileInput = document.getElementById('file');

function isEmpty(table){
    return table.rows.length == 1;
}

verify_visibility();

function verify_visibility(){
    if(!isEmpty(table)){
        tableDiv.style.visibility = 'visible';
        tableResult.style.visibility = 'visible';
        tableDiff.style.visibility = 'visible';
    }else{
        tableDiv.style.visibility = 'hidden';
        tableResult.style.visibility = 'hidden';
        tableDiff.style.visibility = 'hidden';
    }
}

document.getElementById('submitBtn').addEventListener('click', () => {
    verify_visibility();
});

fileInput.addEventListener('change', () => {
  const fileName = fileInput.value
  const fileExtension = fileName.split('.').pop();
  if (fileName !== '' && fileExtension == "csv") {
    submitBtn.disabled = false;
  } else {
    submitBtn.disabled = true;
  }
});

