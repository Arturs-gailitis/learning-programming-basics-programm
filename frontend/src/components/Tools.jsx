import startButtonLogo from '../assets/start-button.svg'
import { postCode } from '../API/apiConnection'

import '../style/Tools.css'

function Tools({ text, setCodeResult}) {

    // nospiežot Start pogu aizsūta kodu un saņem tā rezultātu
    async function runCode() {
        let APIResult = await postCode(text)
        setCodeResult(APIResult.result)
    }

    return (
        <main className='Tools'>
            <div className='ToolList'>
                <button id='startButton' className='ToolButtons' onClick={runCode}>
                    <img src={startButtonLogo}></img>
                </button>
            </div>
        </main>
    )
}

export default Tools