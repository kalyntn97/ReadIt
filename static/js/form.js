const dateInput = document.getElementById('id_expire_on')

const today = new Date()
const tomorrow = new Date(today)
tomorrow.setDate(tomorrow.getDate() + 1)

const picker = MCDatepicker.create ({
  el: '#id_expire_on',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: tomorrow,
  minDate: tomorrow,
})

dateInput.addEventListener('click', (evt) => {
  picker.open()
})