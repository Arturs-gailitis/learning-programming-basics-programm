const ApiAdress = 'http://127.0.0.1:8000'

// aizsūta parasto kodu uz backend un pēc tam dabū tā koda rezultātu
export function postCode(text){

    let result = fetch(ApiAdress + '/code', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({text})
    }).then(response => response.json())

    return result
}