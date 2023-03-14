const tableDiv = document.getElementById('table-div');
const table = document.querySelector('table');
const tableResult = document.getElementById('table-results');
const spanResultTrue = document.getElementById('span-result-true');
const spanResultFalse = document.getElementById('span-result-false');
const lblValidation = document.getElementById('lbl_validation')

function isEmpty(table){
    return table.rows.length == 1;
}
if(isEmpty(table)){
    tableDiv.style.visibility = 'hidden'
    tableResult.style.visibility = 'hidden'
}

document.getElementById('submitBtn').addEventListener('click', () => {
    if(!isEmpty(table)){
        tableDiv.style.visibility = 'visible';
        tableResult.style.visibility = 'visible';
    }else{
        tableDiv.style.visibility = 'hidden';
        tableResult.style.visibility = 'hidden'
    }
});

