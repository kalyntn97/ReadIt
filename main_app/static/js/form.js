const dateInput = document.getElementById('id_expire_on')

const picker = MCDatepicker.create ({
  el: '#id_expire_on',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener('click', (evt) => {
  picker.open()
})