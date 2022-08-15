const menuBar = document.getElementById('menu')
const closeBtn = document.getElementById('close')
const sidebar = document.getElementById('sidebar')

menuBar.addEventListener('click', function () {
    console.log('hello');
    sidebar.style.visibility= 'visible'

})
closeBtn.addEventListener('click', function () {
    sidebar.style.visibility= 'hidden'
})