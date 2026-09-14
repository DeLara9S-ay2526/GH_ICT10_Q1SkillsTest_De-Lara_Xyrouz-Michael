from pyscript import display, document
# Skills test - Reciept Generator


def order(e):

    document.getElementById('result').innerHTML = " "

    item1 = float(document.getElementById('item1').value)
    item2 = float(document.getElementById('item2').value)
    item3 = float(document.getElementById('item3').value)
    item4 = float(document.getElementById('item4').value)

    check1 = document.getElementById('item1').checked
    check2 = document.getElementById('item2').checked
    check3 = document.getElementById('item3').checked
    check4 = document.getElementById('item4').checked

    subtotal = item1 * check1 + item2 * check2 + item3 * check3 + item4 * check4
    
    vat = subtotal * 0.12
    total = subtotal + vat

    display(f'Subtotal {subtotal}', target='result')
    display(f'Total: {total}', target='result')