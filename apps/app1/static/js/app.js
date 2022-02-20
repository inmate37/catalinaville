let users = document.querySelectorAll('.user__info')
users.forEach(user => {
    let role = user.querySelector('#role')
    if(role.innerHTML == "Admin"){
        user.classList.add('user__gold__border')
    }
});