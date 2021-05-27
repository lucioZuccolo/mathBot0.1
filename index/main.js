const loginForm = document.querySelector("#signin-form");

loginForm.addEventListener("submit", (e) =>{
    e.preventDefault();
    const email = document.querySelector("#signin-email").value;
    const password = document.querySelector("#signin-password").value;

    auth
        .signInWithEmailAndPassword(email, password)
        .then(userCredential => {
            
            document.location.href="upload/upload.html"
            loginForm.reset()
            console.log("sign in")
            loginForm.querySelector(".error").innerHTML = ""

        }).catch(err => {
            loginForm.querySelector(".error").innerHTML = err.message;
        })
})

