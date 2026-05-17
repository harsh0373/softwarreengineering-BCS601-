function setInt()
{
   
    var a=document.getElementById("txt2").innerHTML
    var b=document.getElementById("txt3").innerHTML
    var d=document.getElementById("tx1").innerHTML
    var c=document.getElementById("txt1").innerHTML
    
    document.getElementById("txt2").innerHTML=b
    document.getElementById("txt3").innerHTML=a
    document.getElementById("txt1").innerHTML=d
    document.getElementById("tx1").innerHTML=c
    
    var obj1=document.getElementById("img").src;
    var obj2=document.getElementById("img22").src;
    document.getElementById("img").src=obj2
    document.getElementById("img22").src=obj1

    
   
   
}
   

setInterval(setInt,2000);



function img()
{
    var a1=document.getElementById("card1").src
    var a2=document.getElementById("card2").src
    var a3=document.getElementById("card3").src
    var a4=document.getElementById("card4").src
    var b1=document.getElementById("atxt1").innerHTML
    var b2=document.getElementById("btxt1").innerHTML
    var b3=document.getElementById("ctxt1").innerHTML
    var b4=document.getElementById("dtxt1").innerHTML
    var c1=document.getElementById("atxt2").innerHTML
    var c2=document.getElementById("btxt2").innerHTML
    var c3=document.getElementById("ctxt2").innerHTML
    var c4=document.getElementById("dtxt2").innerHTML
    
    document.getElementById("card1").src=a4
    document.getElementById("card2").src=a1
    document.getElementById("card3").src=a2
    document.getElementById("card4").src=a3
   document.getElementById("atxt1").innerHTML=b4
    document.getElementById("btxt1").innerHTML=b1
    document.getElementById("ctxt1").innerHTML=b2
    document.getElementById("dtxt1").innerHTML=b3
    document.getElementById("atxt2").innerHTML=c4
    document.getElementById("btxt2").innerHTML=c1
    document.getElementById("ctxt2").innerHTML=c2
    document.getElementById("dtxt2").innerHTML=c3

}

setInterval(img,3000);



