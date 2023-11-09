const modalRoot = document.getElementById('modal-root')
const loginForm = document.querySelector('.login-form')
// const signupForm = document.querySelector('.signup-form')
const loginBtn = document.getElementById('login-btn')
const closeBtn = document.getElementById('close-btn')

loginBtn.addEventListener('click', () => {
  modalRoot.classList.add('visible')
  // loginForm.classList.add('visible')
})

closeBtn.addEventListener('click', () => {
  modalRoot.classList.remove('visible')
  // loginForm.classList.remove('visible')
})

// modalRoot.addEventListener('click', () => {
//   modalRoot.classList.remove('visible')
// })

// loginForm.addEventListener('click', (e) => {
//   e.preventDefault()
//   e.stopPropagation()
//   e.stopImmediatePropagation()
//   return false
// })

// signupForm.addEventListener('click', (e) => {
//   e.preventDefault()
//   e.stopPropagation()
//   e.stopImmediatePropagation()
//   return false
// })

