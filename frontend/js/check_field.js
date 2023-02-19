function check() {
  if (document.getElementById('search-city').value != '')
    document.getElementById('btncity').removeAttribute('disabled');
  else
    document.getElementById('btncity').disabled='disable';
}


