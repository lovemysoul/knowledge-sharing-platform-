const API = "http://127.0.0.1:5000"


function loadQuestions(){

fetch(API + "/questions")

.then(res=>res.json())

.then(data=>{

let container=document.getElementById("questions")

if(!container) return

container.innerHTML=""

data.forEach(q=>{

container.innerHTML+=`

<div class="question">

<h3>${q.title}</h3>

<p>${q.description}</p>

<b>Category:</b> ${q.category}

</div>

`

})

})

}

if(document.getElementById("questions")){
loadQuestions()
}



function submitQuestion(){

let title=document.getElementById("title").value
let description=document.getElementById("description").value
let category=document.getElementById("category").value

fetch(API + "/ask",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

title:title,
description:description,
category:category

})

})
.then(res=>res.json())
.then(data=>{

alert("Question Added Successfully")

})

}