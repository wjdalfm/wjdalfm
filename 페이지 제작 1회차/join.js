const from = document.getElementById("from")

from.addEventListener("submit", function(event){
    event.preventDefault()

    let uaerId = event.target.id.value
    let uaerpw1 = event.target.pw1.value
    let uaerpw2 = event.target.pw2.value
    let uaername = event.target.name.value
    let uaerphone = event.target.phon.value
    let uaerposition = event.target.position.value
    let uaergender = event.target.gender.value
    varlet uaeremail = event.target.email.value
    let uaerintro = event.target.intro.value

    if(userId,length<6)
        alert("아이디가 너무 짧습니다.6자 이상 입력해주세요")
})