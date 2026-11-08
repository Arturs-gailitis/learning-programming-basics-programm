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

  // funkcija ar kuru viedo indentāciju
  function createIndentation(event) {

    // ja nospieda Tab pogu
    if (event.key == "Tab") {
      
      // atceļ pogas orģinālo darbību, kas nepalīdzēja veidot indentāciju
      event.preventDefault()

      // iegūst redektora objektu
      const redector = event.currentTarget

      // dabū tekstu pirms indentācijas un arī pēc tās
      const startText = text.slice(0, redector.selectionStart)
      const endText = text.slice(redector.selectionEnd)

      // savieno kopā tos kur vidū būs indentācija
      const newText = startText.concat("  ", endText)

      setText(newText)

    } 
  }

  return (
    <main className="redector">
      <div className="textRedector">
        <div className="lineNummeration" ref={lineNumbersRef} aria-hidden="true">
          {Array.from({ length: lineCount }, (_, index) => (
            <span id='lineNumber' key={index}>{addLineCount(index)}</span>
          ))}
        </div>
          <textarea className="redectorTextArea" value={text} onChange={(event) => setText(event.target.value)} onScroll={handleScroll} onKeyDown={createIndentation} wrap="off" spellCheck="false"
        />
      </div>
    </main>
  )
}

export default Redector