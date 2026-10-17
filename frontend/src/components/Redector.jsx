import { useRef } from 'react'
import '../style/Redector.css'

// izveido teksta redektora komponenti
function Redector({ text, setText }) {
  const lineNumbersRef = useRef(null)

  // iegūst kopējo līnijas skaitu tekstā
  const lineCount = text.split('\n').length

  // padara lai vienlaikus teksta laukums un līniju nummerācija ietu uz augšu vai arī uz leju  
  function handleScroll(event) {
    lineNumbersRef.current.scrollTop = event.currentTarget.scrollTop
  }
  
  // ieliek līniju rindā pareizu nummuru
  function addLineCount(index) {
    return index + 1
  }

  return (
    <main className="redector">
      <div className="textRedector">
        <div className="lineNummeration" ref={lineNumbersRef} aria-hidden="true">
          {Array.from({ length: lineCount }, (_, index) => (
            <span id='lineNumber' key={index}>{addLineCount(index)}</span>
          ))}
        </div>
        <textarea className="redectorTextArea" value={text} onChange={(event) => setText(event.target.value)}
          onScroll={handleScroll} wrap="off" spellCheck="false"
        />
      </div>
    </main>
  )
}

export default Redector