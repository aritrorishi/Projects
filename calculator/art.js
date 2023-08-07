 

 let string = "";
 let string2 = "";
 let arr= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

 let buttons = document.querySelectorAll('.button');
Array.from(buttons).forEach((button)=>{
    button.addEventListener('click', (e) => {
        if(e.target.innerHTML == "="){
            string2 = string2+e.target.innerHTML;

            string = eval(string);
            document.querySelector('.input').value = string;
           

        }
        else if(e.target.innerHTML == "X"){
            
            string2 = string + "X";
            string = string + "*";
            document.querySelector('.input').value = string2;
        }
        else{
            console.log(e.target);
            if(string2.includes('=') && arr.includes(e.target.innerHTML)){
                string2 = "";
                string = "";
                string2 = e.target.innerHTML;
                string = e.target.innerHTML;

            }
            
            else{
                
                string = string + e.target.innerHTML;
                string2 = string2 + e.target.innerHTML;
            }
            document.querySelector('.input').value = string2;
        }
    })
})