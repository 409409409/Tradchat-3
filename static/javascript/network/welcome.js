cl = io()

cl.connect('http://'+document.domain+':'+location.port)

function recv(message) {
    msg = eval(message)
    
    if (msg[0] == 'Create Account Results') {
        if (msg[2] == 'Success') {
            closeLoginModal()
        }
    }
}

function SignUpPressed(e) {
    cl.send(JSON.stringify(['Create Account', [e.username, e.password, e.first_name, e.last_name, e.email, e.dob, e.gender]]))
}

function LogInPressed(e) {
    cl.send(JSON.stringify(['Log In', {'username': e.username, 'password': e.password}]))
}

cl.on('message', recv)