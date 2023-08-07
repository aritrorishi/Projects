let string = "";
let state = false;

let arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
let arr2 = [ '/', '+', '-', '*'];
 

 let buttons = document.querySelectorAll('.button');
Array.from(buttons).forEach((button)=>{
    button.addEventListener('click', (e) => {
        if(e.target.innerHTML == "="){
            state = true;
            
            document.querySelector('.input').value = eval(string);
        }
        // else if(e.target.innerHTML == "x"){
        //     if(string.includes('+') || string.includes('-') || string.includes('/') || string.includes('*')){
        //         string= eval(string);
        //         string = string + '*';
        //         document.querySelector('.input').value = string;
        //     }
        //     else{
        //         string = string + '*';
        //         state = false;
        //         document.querySelector('.input').value = string;
        //     }
            
        // }
        else if(arr.includes(e.target.innerHTML)){
            
            if(state == true){
                string = "";
                string = string + e.target.innerHTML;            
                state = false;
            }
            else{
                string = string + e.target.innerHTML;           
            }
            document.querySelector('.input').value = string;
        }
        
        else{
            for(let i = 0; i < string.length - 1; i++){
                if(arr2.includes(string[i]) && arr2.includes(string[i+1])){
                    alert("invalid input");
                    string = "";
                    document.querySelector('.input').value = string;

                }
                break;
            }
            console.log(e.target);
            string = eval(string) + e.target.innerHTML;
            document.querySelector('.input').value = string;
            state = false;
        }
       
    })
})