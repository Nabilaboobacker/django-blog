
function validateForm(){
let search_keyword = document.getElementById("search_keyword").value.trim();
if (search_keyword === ''){
    alert("Enter something");
    return false;
}
return true;
}