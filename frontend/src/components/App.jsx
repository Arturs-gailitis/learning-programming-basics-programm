import { useState } from 'react'

import Redector from './Redector.jsx'
import Tools from './Tools.jsx'
import Console from './Console.jsx'
import DataInfo from './DataInfo.jsx'

import '../style/App.css'

function MainApp() {
  const [text, setText] = useState('')
  const [codeResult, setCodeResult] = useState([])
  const [codeData, setCodeData] = useState({})

  return (
    <main>
      <Tools text={text} setText={setText} setCodeResult={setCodeResult} setCodeData={setCodeData} />
      <div id='redectorLayout'>
        <Redector text={text} setText={setText} />
        <DataInfo data={codeData} />
      </div>
      <Console codeResult={codeResult} />
    </main>
  )
}

export default MainApp