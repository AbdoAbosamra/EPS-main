const url = window.location.href

console.log(url)

const  quizBox = document.getElementById('quiz-box')
const  scoreBox = document.getElementById('score-box')
const  resultBox = document.getElementById('result-box')
let data

$.ajax({
    type:'GET',
    url : `${url}data`,
    success: function (response){
        console.log(response)
        const data = response.data
        data.forEach(el => {
            for (const [question,answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2 bg-warning">
                        <p class="fs-1 fw-bold text-dark ">${question}</p>
                        <hr>
                    </div>
                `

                answers.forEach(answer => {
                    quizBox.innerHTML += `
                    
                    <div class="container mb-2 bg-info">
                        <input type="radio" class="ans bg-danger" id="${question} - ${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>
                `
                })
            }
        });
    },
    error:function(error){
        console.log(error)
    }
})


const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')



const sendData = () =>{
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el =>{
        if (el.checked){
            data[el.name] = el.value
        }else{
            if (!data[el.name]){
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type:'POST',
        url: `${url}sava/`,
        data : data,
        success : function(response){
            const results = response.results
            console.log(results)
            quizForm.style.visibility = 'hidden'


            scoreBox.innerHTML = `${response.passed ? 'Congratulations !' : 'Ops ..'} Your result id ${response.score.toFixed(2)}`


            results.forEach(res =>{
                const resDiv = document.createElement("div")
                for(const [question,resp] of Object.entries(res)){
                    resDiv.innerHTML += question
                    const cls =['container','p-3','text-light','h3']
                    resDiv.classList.add(...cls)


                    if (resp== 'not answered'){
                        resDiv.innerHTML += '- not answered'
                        resDiv.classList.add('bg-danger')
                    }else{
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct){
                            resDiv.innerHTML += ` --> answered: ${answer} `
                            resDiv.classList.add('bg-success')
                        }else{
                            resDiv.innerHTML += ` --> correct answer: ${correct}`
                            resDiv.innerHTML += `--> answered: ${answer}`
                            resDiv.classList.add('bg-danger')
                        }
                    }
                }
                document.getElementById('score-box').style = "position:absolute; top:130px"
                document.getElementById('result-box').style = "position:absolute; top:200px"
                resultBox.append(resDiv)

            })
             //document.getElementsByClassName('result').style.position = 'absolute'
             //document.getElementsByClassName('result').style.position.top('200px')

        },
        error:function(error){
        console.log(error)
    }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    $("html, body").animate({ scrollTop: 0 }, "slow");
    sendData()
} )




