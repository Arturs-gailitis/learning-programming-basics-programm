import { useState } from 'react'

import Redector from './Redector.jsx'
import Tools from './Tools.jsx'
import Console from './Console.jsx'
import DataInfo from './DataInfo.jsx'
import Tutorial from './Tutorial.jsx'

import '../style/App.css'

function MainApp() {

  // priekš datu pārvietošanas
  const [text, setText] = useState('')
  const [codeResult, setCodeResult] = useState([])
  const [codeData, setCodeData] = useState({})

  // priekš statusa maiņas programmā
  const [tutorialState, setTutorialState] = useState(false)

  return (
    <main>
      {tutorialState == true ? (
        <Tutorial setTutorialState={setTutorialState}/>
      ) : (
      <>
        <Tools text={text} setText={setText} setCodeResult={setCodeResult} setCodeData={setCodeData} setTutorialState={setTutorialState}/>
        <div id='redectorLayout'>
          <Redector text={text} setText={setText} />
          <DataInfo data={codeData} />
        </div>
        <Console codeResult={codeResult} />
      </>
      )}
    </main>
  )
}

export default MainApp