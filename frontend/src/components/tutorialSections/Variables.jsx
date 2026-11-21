import '../../style/TutorialSection.css'

function Variables() {

    const code1 = 'mainigais vards = "Pēteris"' + '\n' + 'mainigais vecums = 21'
    const code2 = 'mainigais x = 3' + '\n' + 'x = 13'
    const code3 = 'printet("Sveika pasaule")' + '\n' + 'mainigais cipars = 2' + '\n' + 'printet(cipars)' + '\n' + 'printet("Rezultāts: " + cipars)'
    const code4 = 'mainigais brauc = patiess' + '\n' + 'mainigais brauc = nepatiess'

    return (
        <main className='Content'>
            <h2>Mainīgie un printēšana</h2>

            <div className='TutorialArticle'>

                <p>
                    Programmēšanā mainīgais ir nodefinēts nosaukums, kur saglabāta konkrēta vērtība.
                    Saglabātā vērtība var būt skaitlis, teksts, loģiskā vērtība vai arī masīvs (skaties 8. pamācības nodaļu). 
                </p>

                <h3>Mainīgā izveidošana</h3>
                <p>
                    Lai izveidotu mainīgo ir jāizmanto atslēgvārds <b>mainigais</b>.
                    Pēc šī atslēgvāda ir jāraksta mainīgā nosaukums un vērtība. 
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <p>
                    Šajā piemērā tika izveidoti divi mainīgie: <b>vards</b> satur teksta vērtību, bet <b>vecums</b> satur 
                    cipara vērtību.
                </p>

                <h3>Parasto vērtību datu tipi</h3>
                <ul>
                    <li>
                        <p>
                            Vesels skaitlis: <div className='codeTextArea'>{'mainigais skaits = 10'}</div>
                        </p>
                    </li>
                    <li>
                        <p>
                            Daļskaitlis: <div className='codeTextArea'>{'mainigais cena = 1.56'}</div>
                        </p>
                    </li>
                    <li>
                        <p>
                            Teksts: <div className='codeTextArea'>{'mainigais nosaukums = "Piens"'}</div>
                        </p>
                    </li>
                    <li>
                        <p>
                            Loģiskā vērtība: <div className='codeTextArea'>{code4}</div>
                        </p>
                    </li>
                </ul>

                <h3>Mainīgo izmantošana</h3>
                <p>
                    Pēc nodefinēšanas, mainīgos var izmantot citās komandās.
                    Lai izmantotu konkrētu mainīgo ir nepieciešams tikai uzrakstīt tā nosaukumu.
                    Nodefinētam mainīgajam, var nomainīt tā vērtību.
                    Tadā situācijā vairs neizmanto atslēgvārdu <b>mainigais</b>.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <h3>Rezultāta izvadīšana konsolē</h3>
                <p>
                    Lai koda rezultāts parādītos konsolē, ir jāizmanto funkcija <b>printet()</b>.
                    Vienkārš teksts ir jāieliek pēdiņās, bet cipars var būt bez tās.
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Rezultātā konsolē parādīsies atbilde šādā secībā:
                </p>

                <ol>
                    <li>Sveika Pasaule</li>
                    <li>2</li>
                    <li>Rezultāts: 2</li>
                </ol>
            </div>
        </main>
    )
}

export default Variables