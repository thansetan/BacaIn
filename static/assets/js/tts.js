if (!('speechSynthesis' in window)) {
    alert(
        'baca sendiri ya, browsermu belum mendukung buat fitur baca nya BacaIn. WKWKWKWKKWK'
    )
    tombol = document.getElementById('tts')
    tombol.classList.add('disabled')
}
let myTimeout
myTimer = () => {
    window.speechSynthesis.pause()
    window.speechSynthesis.resume()
    myTimeout = setTimeout(myTimer, 10000)
}
let Teks = document.getElementById('hasil_ocr').innerHTML
$(() => {
    window.speechSynthesis.cancel()
    myTimeout = setTimeout(myTimer, 10000)
    const utt = new SpeechSynthesisUtterance(Teks)
    $('a#tts').on('click', (e) => {
        e.preventDefault()
        utt.lang = bahasa
        utt.onend = () => {
            clearTimeout(myTimeout)
        }
        window.speechSynthesis.speak(utt)
    })
})
