const menuBar = document.getElementById('menu0')
const closeBtn = document.getElementById('close')
const sidebar = document.getElementById('sidebar')

menuBar.addEventListener('click', function () {
    sidebar.style.visibility= 'visible'

})
closeBtn.addEventListener('click', function () {
    sidebar.style.visibility= 'hidden'
})