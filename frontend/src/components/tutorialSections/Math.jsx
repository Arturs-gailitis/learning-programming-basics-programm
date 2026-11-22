import '../../style/TutorialSection.css'

function Math() {

    const code1 = 'mainigais x = 10' + '\n' + 'mainigais y = x + 4'
    const code2 = 'mainigais rezultāts = 5 + 3 * 2' + '\n' + 'mainigais summa = (5 + 3) * 2'
    const code3 = 'mainigais x = "Sveika"' + '\n' + 'mainigais y = "Pasaule"' + '\n' + 'mainigais rezultats = x + " " + y'

    return (
        <main className='Content'>
            <h2>Matemātiskās operācijas</h2>

            <div className='TutorialArticle'>

                <p>
                    Pseidokodā var arī aprēķināt skaitliskas vērtības izmantojot matemātiskas darbības.
                    Konkrētās matemātiskās darbības var veikt ar skaitļiem, gan ar nodefinētiem mainīgajiem, kā 
                    arī speciālā gadījumā, kad vajag abus tekstus savienot vienā vērtībā.
                </p>

                <h3>Matemātiskie simboli</h3>

                <p>
                    Šīs mācību programmas pseidokods atbalsta visas 4 pamata matemātiskās darbības:
                </p>

                <ul>
                    <li>saskaitīšana ar <b>+</b> simbolu <div className='codeTextArea'>{'mainigais x = 2 + 4'}</div></li>
                    <li>atņemšana ar <b>-</b> simbolu <div className='codeTextArea'>{'mainigais y = 10 - 5'}</div></li>
                    <li>reizināšana ar <b>*</b> simbolu <div className='codeTextArea'>{'mainigais z = 10 * 3'}</div></li>
                    <li>dalīšana ar <b>/</b> simbolu <div className='codeTextArea'>{'mainigais a = 6 / 2'}</div></li>
                </ul>

                <p>
                    Šajos 4 dotajos piemēros, katrās matemātiskās darbības rezultāts, tiek saglabāts jaunā mainīgāgajā.
                    Tāpēc matemātiskās operācijas var izmantot, lai izveidotu citus mainīgos. 
                </p>

                <h3>Matemātiskās darbības izmantojot mainīgos</h3>

                <p>
                    Matemātiskā procesā var izmantot jau iepriekš izveidotus mainīgos, nevis tikai skaitļus.
                    Šajā situācijā, programma aprēķinās izmantojot mainīgā saglabāto vērtību. 
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <h3>Matemātisko darbību izpildes secība</h3>

                <p>
                    Tā pat kā tas ir matemātikā, tad arī šeit reizināšana un dalīšana būs pirmās, kuras izpildīsies.
                    Pēc tam tikai saskaitīšana un atņemšana. Ja grib izmainīt izpildes secību, tad izmanto iekavas.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Rezultātā mainīgais <b>rezultāts</b> būs 11, jo reizināšana izpildās pirmā.
                    Bet mainīgais <b>summa</b> būs 16, jo darbība, kas atrodās iekavās, izpildīsies pirmā.
                </p>

                <h3>Darbība ar atlikumu</h3>

                <p>
                    Lai varētu iegūt dalīšanas atlikumu, tiek izmantots atslēgvārds <b>atlikums</b>.
                    Izmantojot šo atslēgvārdu, atgrizīs vērtību, kas vairākas reizes daloties, paliks kā atlikums.
                </p>

                <div className='codeTextArea'>
                    {'mainigais f = 10 atlikums 3'}
                </div>

                <p>
                    Rezultātā mainīgais <b>f</b> būs 1, jo 10 nedalās ar 3, bet iepriekšējais skaitlis dalās ar 3.
                </p>

                <h3>Teksta savienošana</h3>

                <p>
                    Ja vajag savienot vairākus vērtības, ar teksta datu tipu, kopā. Tad šajā programmā to var izdarīt 
                    izmantojot <b>+</b> zīmi.
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Rezultātā mainīgais <b>rezultats</b> būs Sveika Pasaule.
                </p>
            </div>
        </main>
    )
}

export default Math