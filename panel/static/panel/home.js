const serviceBtns = [...document.getElementsByClassName('service_control')];
serviceBtns.forEach((btn) => {
    btn.addEventListener("click", action);
});
const serverBtns = [...document.getElementsByClassName('server_control')];
serverBtns.forEach((btn) => {
    btn.addEventListener("click", action);
});
const infoBtns = [...document.getElementsByClassName('info')];
infoBtns.forEach((btn) => {
    btn.addEventListener("click", info);
});
const infoCloseBtns = [...document.getElementsByClassName('info_close')];
infoCloseBtns.forEach((btn) => {
    btn.addEventListener("click", info_close);
});

function action(){
    window.location.href = this.getAttribute("data-action").concat("/");
}

function info(){
    const name = this.getAttribute('data-name');
    const infoField = document.getElementById(name.concat("_info_field"));
    const field = [...infoField.getElementsByClassName("info_field")][0];
    console.log(field);
    $.ajax('/info_service/'.concat(name),
        {
            success: function (data) {
                field.innerText = data["info"];
                infoField.classList.remove("d-none");
        }
    });
    
}

function info_close(){
    const field = this.parentElement;
    field.classList.add("d-none");
}