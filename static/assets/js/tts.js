let myTimeout
myTimer = () => {
    window.speechSynthesis.pause()
    window.speechSynthesis.resume()
    myTimeout = setTimeout(myTimer, 10000)
}
let Teks = document.getElementById('hasil_ocr').innerHTML
$(function () {
    window.speechSynthesis.cancel()
    myTimeout = setTimeout(myTimer, 10000)
    const utt = new SpeechSynthesisUtterance(Teks)
    $('a#tts').on('click', function (e) {
        e.preventDefault()
        utt.lang = 'id'
        utt.onend = function () {
            clearTimeout(myTimeout)
        }
        window.speechSynthesis.speak(utt)
    })
})
