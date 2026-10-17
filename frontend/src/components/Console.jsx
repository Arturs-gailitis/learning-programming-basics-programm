import '../style/Console.css'

function Console({codeResult}) {

    const resultLenght = codeResult.length

    return (
        <main className='Console'>
            <div className='TextArea'>
                {Array.from({ length: resultLenght }, (_, index) => (
                    <span className='consoleText' key={index}>{codeResult[index] + "\n"}</span>
                ))}
            </div>
        </main>
    )
}

export default Console
