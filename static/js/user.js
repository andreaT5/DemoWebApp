function setLoginRegisterStatus(bStatus) {
    console.log(bStatus);
    if (bStatus) {
        document.querySelector('.login').classList.add('active');
        document.querySelector('.welcome').classList.add('active');
        document.querySelector('.sign_in').classList.add('active');
        document.querySelector('.btn').classList.add('active');
        document.querySelector('.sign_up').classList.add('active');
    } else {
        document.querySelector('.sign_up').classList.remove('active');
        document.querySelector('.login').classList.remove('active');
        document.querySelector('.welcome').classList.remove('active');
        document.querySelector('.sign_up').classList.remove('active');
        document.querySelector('.btn').classList.remove('active');
        document.querySelector('.sign_in').classList.remove('active');
    }
}

setLoginRegisterStatus(true);