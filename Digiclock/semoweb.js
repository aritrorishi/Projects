let a;
let str = "";
let hr = "";
let min = "";
let sec = "";
let dhr = "";
let dmin = "";
let dsec = "";
function padnum(num){
    if(num < 10){
        return "0" + num ;
    }
    else{
        return num;
    }
}
setInterval(clock, 1000);
function clock(){
 a = new Date();
 hr = (a.getHours())%12;
 min = a.getMinutes();
 sec = a.getSeconds();

 dhr = padnum(hr);
 dmin = padnum(min);
 dsec = padnum(sec);
 
 if(a.getHours() > 12){
    str = dhr +" : "+ dmin +" : " + dsec + " PM";
 }
 else{
    str = dhr +" : "+ dmin +" : " + dsec + " AM";
 }
 
 
 document.querySelector('.input').value = str;
}