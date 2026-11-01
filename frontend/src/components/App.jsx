import { useState } from 'react'

import Redector from './Redector.jsx'
import Tools from './Tools.jsx'
import Console from './Console.jsx'

function MainApp() {
  const [text, setText] = useState('')
  const [codeResult, setCodeResult] = useState([])

  return (
    <main>
      <Tools text={text} setText={setText} setCodeResult={setCodeResult} />
      <Redector text={text} setText={setText} />
      <Console codeResult={codeResult} />
    </main>
  )
}

export default MainApp