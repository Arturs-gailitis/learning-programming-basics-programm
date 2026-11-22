import '../../style/TutorialSection.css'

function Array() {

    const code1 = 'mainigais skaitli = [1, 2, 3, 4]' + '\n' + 'mainigais vardi = ["viens", "divi", "trīs"]' + '\n' + 'mainigais tukss = []'
    const code2 = 'mainigais skaitli = [10, 20, 30]' + '\n' + 'mainigais x = skaitli[0]' + '\n' + 'mainigais y = skaitli[2]' + '\n' + 'printet(x)' + '\n' + 'printet(y)'
    const code3 = 'mainigais skaitli = [1, 2, 3]' + '\n' + 'skaitli[1] = 10' + '\n' + 'printet(skaitli)'
    const code4 = 'mainigais skaitli = [1, 2]' + '\n' + 'ielikt(skaitli, 3)' + '\n' + 'ielikt(skaitli, 4)' + '\n' + 'printet(skaitli)'
    const code5 = 'mainigais skaitli = [1, 2, 3, 4]' + '\n' + 'izmest(skaitli)' + '\n' + 'printet(skaitli)'
    const code6 = 'mainigais skaitli = [1, 5, 7]' + '\n' + 'mainigais i = 0' + '\n' + 'kamer i mazaks izmers(skaitli) tad' + '\n' + '    printet(skaitli[i])' + '\n' + '    i = i + 1' + '\n' + 'beigas'

    return (
        <main className='Content'>
            <h2>Darbošanās ar masīvu</h2>

            <div className='TutorialArticle'>

                <p>
                    Masīvs ir datu tips, kur glabājās vairākas tās pašas datu tipa vertības.
                    Programmas pseidokodā, masīva vērtības raksta ar kvadrātiekavām un atdala katru ar komatu.
                </p>

                <h3>Masīva izveidošana</h3>
                <p>
                    Masīvu izveido tā pat kā citus mainīgos, tikai vērtības vietā būs kvadrātiekavās.
                    Masīvā var glabāt skaitļus, tekstu un loģiskās vērtības. Lai izveidotu tukšu masīvu, izmanto <b>[]</b>.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <h3>Masīva elementu iegūšana</h3>
                <p>
                    Lai iegūtu elementu no masīva ir jāizmanto indekss, kas sākas ar 0.
                    Indekss ir jāieliek iekšā kvadrātiekavās, jau nodefinētā masīvā.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Šajā piemērā <b>x</b> iegūst vērtību 10, bet <b>y</b> - vērtību 30.
                </p>

                <h3>Masīva elementa vērtības mainīšana</h3>
                <p>
                    Esošo elementu masīvā var nomainīt izmantojot indeksu
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Pēc šīs darbības masīva otrais elements ar indeksu 1 atradīsies vērtība 10 nevis vērtība 2.
                </p>

                <h3>Elementa pievienošana masīvam</h3>
                <p>
                    Lai masīvā pievienotu jaunu elementu, izmanto funkciju <b>ielikt()</b>.
                    Pirmais funkcijas arguments ir masīva nosaukums, bet otrais — pievienotā vērtība.
                </p>

                <div className='codeTextArea'>
                    {code4}
                </div>

                <p>
                    Funkcija <b>ielikt()</b> pievieno tikai vērtības masīva beigās, tāpēc pēc koda izpildes masīvs būs [1, 2, 3, 4].
                </p>

                <h3>Pēdējā elementa izņemšana</h3>
                <p>
                    Lai no masīva izņemtu elementu, izmanto funkciju <b>izmest()</b>.
                    Šī funkcija saņem vienu argumentu — tā masīva nosaukumu, no kura jāizņem elements.
                </p>

                <div className='codeTextArea'>
                    {code5}
                </div>

                <p>
                    Pēc <b>izmest()</b> izpildes masīvā paliks [1, 2, 3], jo <b>izmest()</b> tikai noņem 
                    pēdējo elementu no masīva.
                </p>

                <h3>Masīva garuma iegūšana</h3>
                <p>
                    Izmantojot funkcija <b>izmers()</b> atgriezīs kopējo masīva elementu skaitu.
                    To var izmantot aprēķinos, nosacījumos un ciklu robežās, tā lai apstrādātu visus masīva elementus.
                </p>

                <div className='codeTextArea'>
                    {code6}
                </div>

                <p>
                    Šajā piemērā <b>kamer</b> cikls izvadīs visus masīva elementus, nezinot cik daudz masīvā atrodās elementi.
                </p>
            </div>
        </main>
    )
}

export default Array