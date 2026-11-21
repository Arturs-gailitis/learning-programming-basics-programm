import { useRef } from 'react'

import startButtonLogo from '../assets/start-button.svg'
import cleanButtonLogo from '../assets/clean-button.svg'
import openFileButtonLogo from '../assets/open-file-button.svg'
import saveFileButtonLogo from '../assets/save-file-button.svg'
import tutorialButtonLogo from '../assets/tutorial-button.svg'

import { postCode } from '../API/apiConnection'

import '../style/Tools.css'

function Tools({ text, setText, setCodeResult, setCodeData, setTutorialState}) {

    const fileInput = useRef(null)

    // nospiežot Start pogu aizsūta kodu un saņem tā rezultātu
    async function runCode() {
        let APIResult = await postCode(text)
        
        setCodeResult(APIResult.result)
        setCodeData(APIResult.data)
    }

    // nospiežot tiek izdzēsts koda teksts un rezultāts
    function clearText() {
        setText('')
        setCodeResult([''])
        setCodeData({})
    }

    // iegūst kodu no .txt faila
    async function getCodeFromFile(event) {

        const userFile = event.target.files[0];

        try {
            
            // iegūst faila tekstu
            const code = await userFile.text();

            setText(code)

        } catch {
            return
        }
    }

    // nolādē pseidokodu .txt failā
    function saveCode() {

        // izveido teksta objektu un arī to lokālo adressi
        const blob = new Blob([text], { type: 'text/plain;charset=utf-8' })
        const localUrl = URL.createObjectURL(blob)

        // izveido šī faila linku un automātiski nospiež to
        const fileLink = document.createElement('a')
        fileLink.href = localUrl
        fileLink.download = 'fails.txt'
        fileLink.click()

        // atceļ lokālo linku
        URL.revokeObjectURL(localUrl)
    }

    return (
        <main className='Tools'>
            <div className='ToolList'>
                <button id='startButton' className='ToolButtons' onClick={runCode} title='Izpildīt kodu'>
                    <img src={startButtonLogo}></img>
                </button>
                <button id='cleanButton' className='ToolButtons' onClick={clearText} title='Sākt no jauna'>
                    <img src={cleanButtonLogo}></img>
                </button>
                <button id='gettingCodeButton' className='ToolButtons' onClick={() => fileInput.current.click()} title='Iegūt pseidokodu no .txt faila'>
                    <img src={openFileButtonLogo}/>
                </button>
                <button id='saveCodeButton' className='ToolButtons' onClick={saveCode} title='Saglabāt kodu'>
                    <img src={saveFileButtonLogo}/>
                </button>
                <button id='tutorialButton' className='ToolButtons' onClick={() => setTutorialState(true)} title='Skatīt instrukciju un uzdevumus'>
                    <img src={tutorialButtonLogo}/>
                </button>
            </div>
            <input className='fileInput' ref={fileInput} type='file' accept='.txt' onChange={getCodeFromFile}></input>
        </main>
    )
}

export default Tools
