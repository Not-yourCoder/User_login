function validate(){
    // password validation on form live update text
    function detect(){
        let x = document.getElementById("password").value;
        let y = document.getElementById("cpassword").value;
        if(x === y){
            if(x && y == " "){
                document.getElementById("text").innerText = "passwords cannot be empty";
                document.getElementById("text").style.color = "red";
            }
            else{
                document.getElementById("text").innerText = "Password Matching";
                document.getElementById("text").style.color = "green";

            }
        }

        // else if(x || y == " "){
        //     document.getElementById("text").innerText = "Password cannot be empty."
        //     document.getElementById("text").style.color  = "red"
        // }
        
        else{
            document.getElementById("text").innerText = "Password Mismatch";
            document.getElementById("text").style.color = "red";
        }

        }
        detect()

        // radio button check

        function radio(){
        let len = document.getElementById("password").value;
        if(len.length >= 8){
            document.getElementById("rd_btn1").checked = true;
        }
        
        }
        radio()

        function hasLowercase(){
            let len = document.getElementById("password").value;
            const lowerregex = /[a-z]/;
            if(lowerregex.test(len)){
                document.getElementById("rd_btn3").checked = true;
            }
        }
        hasLowercase()
            
        
        function hasUppercase(){
            let len = document.getElementById("password").value;
            const upperregex = /[A-Z]/;
            if(upperregex.test(len)){
                document.getElementById("rd_btn2").checked = true;
            }
        }
        hasUppercase()
     // check for symbols in password

     function has_Symbols(){
        let len = document.getElementById("password").value;
        const symbol_regex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/ && /\d/ ;
        if(symbol_regex.test(len)){
            document.getElementById("rd_btn4").checked = true;
        }
    }
    has_Symbols()

}


