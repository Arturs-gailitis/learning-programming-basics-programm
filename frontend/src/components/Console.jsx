import '../style/Console.css'

function Console({codeResult}) {

    const resultLenght = codeResult.length

    // pārtaisa rezultātu no masīva uz string
    function fixResultFormat(result) {

        let resultText = result[0];

        for (let i = 1; i < resultLenght; i++) {
            resultText = resultText + '\n' + result[i];
        }

        return resultText
    }

    return (
        <main className='Console'>
            <div id='Header'>Konsole</div>
            <textarea value={fixResultFormat(codeResult)} className='TextArea' readOnly wrap='off'></textarea>
        </main>
    )
}

export default Console