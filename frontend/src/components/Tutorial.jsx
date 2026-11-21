import { useState, useRef } from 'react'

import '../style/Tutorial.css'

function Tutorial({ setTutorialState }) {

    const [tutorialSection, setTutorialSection] = useState(0)
    const [tutorialName, setTutorialName] = useState('')

    const buttonRef = useRef(null)

    const titles = [
        'Mainīgie un printēšana',
        'Matemātiskās operācijas',
        'Loģiskās operācijas',
        'Salīdzināšanas bloki',
        'Atkārtošanas bloks ar zināmu robežu',
        'Atkārtošanas bloks ar nezināmu robežu',
        'Funkciju definēšana un izmantošana',
        'Darbošanās ar masīvu'
    ]

    function createTutorialContentButtons() {

        const count = titles.length

        let contentaList = []

        for (let i = 0; i < count; i++) {

            contentaList.push(
                <button key={i} className='tutorialContentButton' onClick={() => changeTutorialSectionState(i + 1)}>
                    {(i + 1) + ". " + titles[i]}
                </button>
            )
        }

        return contentaList
    }

    function changeTutorialSectionState(section) {

        switch (section) {

            case (0):
                setTutorialName("Pamācības Satura Rādītājs")
                setTutorialSection(0)
                break
            
            case (1):
                setTutorialName(titles[0])
                setTutorialSection(1)
                break

            case (2):
                setTutorialName(titles[1])
                setTutorialSection(2)
                break

            case (3):
                setTutorialName(titles[2])
                setTutorialSection(3)
                break

            case (4):
                setTutorialName(titles[3])
                setTutorialSection(4)
                break

            case (5):
                setTutorialName(titles[4])
                setTutorialSection(5)
                break

            case (6):
                setTutorialName(titles[5])
                setTutorialSection(6)
                break

            case (7):
                setTutorialName(titles[6])
                setTutorialSection(7)
                break

            case (8):
                setTutorialName(titles[7])
                setTutorialSection(8)
                break
        }
    }

    function showTutorialSection (sectionNumber) {

        switch (sectionNumber) {

            case (1):
                break
        }
    }

    return (
        <main className='Tutorial'>
            <div className='tutorialHeader'>
                <h1 id='tutorialTitle'>{tutorialName == '' ? "Pamācības Satura Rādītājs" : tutorialName}</h1>

                {tutorialSection == 0 ? (
                    <button className='exitButton' onClick={() => setTutorialState(false)}>Atgriezties</button>
                ) : (
                    <button className='exitButton' onClick={() => changeTutorialSectionState(0)}>Atgriezties uz pamācības saturu</button>
                )}

            </div>

            {tutorialSection == 0 ? (
                <div className='tutorialContent'>
                    <h2>Saturs</h2>
                    <div className='tutorialContentButtons'>
                        {createTutorialContentButtons()}
                    </div>
                </div>
            ) : (
                showTutorialSection(tutorialSection)
            )}
        </main>
    )
}

export default Tutorial