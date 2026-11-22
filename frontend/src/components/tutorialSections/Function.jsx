import '../../style/TutorialSection.css'

function Function() {

    const code1 = 'funkcija testēšana():' + '\n' + '    printet("Sveika pasaule!")' + '\n' + 'funkcijas beigas' + '\n' + 'testēšana()'
    const code2 = 'funkcija arguments(teksts):' + '\n' + '    printet("Sveiks, " + teksts)' + '\n' + 'funkcijas beigas' + '\n' + 'arguments("Jāni")'
    const code3 = 'funkcija matemātika(x, y):' + '\n' + '    mainigais summa = x + y' + '\n' + '    printet(summa)' + '\n' + 'funkcijas beigas' + '\n' + 'matemātika(1, 9)'
    const code4 = 'atgriezta funkcija reiz(x, y):' + '\n' + '    mainigais r = x * y' + '\n' + '    atgriezt r' + '\n' + 'funkcijas beigas' + '\n' + 'mainigais rezultats = reiz(3, 5)' + '\n' + 'printet(rezultats)'

    return (
        <main className='Content'>
            <h2>Funkciju definēšana un izmantošana</h2>

            <div className='TutorialArticle'>

                <p>
                    Funkcija ir nosaukts koda daļa, kuru tikai ir jāizveido vienu reizi, bet var izmantot vairākas reizes.
                    Izmantojot funkcijas, var samazināt koda apjomu un padarīt vairāk pārskatāmu.
                </p>

                <h3>Funkcijas izveidošana</h3>
                <p>
                    Lai izveidotu parastu funkciju, vispirms ir jāraksta atslēgvārds <b>funkcija</b>, 
                    pēc tās jāuzraksta unikāls funkcijas nosaukums un iekavas. 
                    Funkcijas definētās rindas beigās jāuzraksta kols, bet funkciju noslēdz ar atlsēgvādiem <b>funkcijas beigas</b>.
                    Funkcijas nosaukums ir jābūt tādam, lai saprastu tā darbību.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <p>
                    Kods kas atrodās funkcijā netiek izpildīta, kad šo funkciju nodefinē.
                    Tas tikai tiek izpildīts, kad konkrēto funkciju izsauc.
                </p>

                <h3>Funkcijas parametri</h3>
                <p>
                    Iekavās var norādīt parametrus, jeb lokālās vērtības, kuras funkcija saņem funkciju izsaukšanas brīdī.
                    Funkcijas iekšienē parametrus var izmantot tāpat kā pārējos mainīgos.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Izsaucot funkciju <b>argumenti()</b>, teksts <b>Jāni</b> tiek nodots parametram <b>teksts</b>.
                    Vienai funkcijai var būt arī vairāki parametri.
                </p>

                <h3>Funkcijas izmantošana ar vairākiem parametriem</h3>
                <p>
                    Ja funkcijai ir vairāki parametri, izsaukumā vērtības jānorāda tādā secībā, kā tās tika definētas
                    Funkcija var izmantot šīs vērtības aprēķinos salīdzināšanā vai arī izprintēt konsolē.
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Funkcija 1 un 9 saskaitīs un konsolē izvadīs rezultātu 10.
                </p>

                <h3>Rezultāta atgriešana</h3>
                <p>
                    Ja funkcijai ir jāatgriež rezultāts, tās definīcijas sākumā jāizmanto atslēgvārdus <b>atgriezta funkcija</b>.
                    Lai atgrieztu vērtību izsaukšanas vietā, funkcijas iekšienē jāizmanto atslēgvārds <b>atgriezt</b> un 
                    tālāk vajadzīgā vērtība.
                </p>

                <div className='codeTextArea'>
                    {code4}
                </div>

                <p>
                    Funkcija <b>reiz()</b> atgriež reizināšanas rezultātu. Atgriezto vērtību var saglabāt mainīgajā.
                </p>
            </div>
        </main>
    )
}

export default Function